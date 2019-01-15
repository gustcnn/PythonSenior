# --*--coding:utf-8
# Author:cnn
import socket
import os
import time
import re
import select

"""单进程、单线程非阻塞并发实现web服务器"""
CLRF = "\r\n"
OBJECT_PATH = os.path.dirname(os.path.dirname(__file__))


# print(OBJECT_PATH)


class WebServer(object):
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 8080
        self.socket_list = list()
        self.epoll=None

    def service_handler(self, client_socket, recv_data):
        recv_data_str = recv_data.decode("utf8")
        print(recv_data_str)
        if recv_data:
            # 获得请求头的第一行,即GET HTTP/1.1 200 OK
            recv_data_list = recv_data_str.splitlines()
            # print(recv_data_list)
            if len(recv_data_list) != 0:
                recv_data_get = recv_data_list[0]
                re_html = r"[^/]+(/[^ ]*)"
                re_html_result = re.match(re_html, recv_data_get)
                file_name = None
                # 判断正则匹配结果,匹配到了,获得匹配的值,如果浏览器输入/则默认返回index.html
                if re_html_result:
                    file_name = re_html_result.group(1)
                    if file_name == "/":
                        file_name = "/index.html"
                try:
                    file = open(OBJECT_PATH + "/htmls" + file_name, "rb")
                except:
                    response_404 = "HTTP/1.1 404 NOT FOUND" + CLRF
                    response_404 += "Content-Type:text/html;charset=utf-8" + CLRF
                    response_404 += CLRF
                    client_socket.send(response_404.encode("utf8"))
                    try:
                        file_404 = open(OBJECT_PATH + "/htmls/404.html", "rb")
                        content_404 = file_404.read()
                        client_socket.send(content_404)
                    except:
                        print("页面不存在")
                    else:
                        file_404.close()
                else:
                    response = "HTTP/1.1 200 OK" + CLRF
                    response += "Content-Type:text/html;charset=utf-8" + CLRF
                    response+="Content-length:"+str(len(recv_data_str))+CLRF
                    response += CLRF
                    # 返回响应头给浏览器
                    client_socket.send(response.encode("utf8"))
                    html_content = file.read()
                    client_socket.send(html_content)
                    file.close()
                    client_socket.close()

        else:
            client_socket.close()

    def main(self):
        # 创建socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定ip
        server_socket.bind((self.ip, self.port))
        # 创建监听
        server_socket.listen()
        # 将此socket设置成非阻塞
        server_socket.setblocking(False)
        #创建一个epoll对象
        self.epoll=select.epoll()
        #将server_socket的fd注册到epoll中
        self.epoll.register(server_socket.fileno(),select.EPOLLIN)
        #定义一个字典存储fd:socket
        fd_event_dict=dict()
        while True:
            #阻塞,直到操作系统告知有事件
            fd_event_list=self.epoll.poll()
            for fd,event in fd_event_list:
                if fd==server_socket.fileno():
                    # 循环接收客户端连接
                    request_socket, request_ip = server_socket.accept()
                    self.epoll.register(request_socket.fileno(), select.EPOLLIN)
                    fd_event_dict[request_socket.fileno()]=request_socket
                #判断已经连接的客户端是否有数据发送过来
                elif event==select.EPOLLIN:
                        recv_data = fd_event_dict[fd].recv(1024)
                        self.service_handler(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    self.epoll.unregister(fd)
                    del fd_event_dict[fd]


if __name__ == '__main__':
    web_server = WebServer()
    web_server.main()

