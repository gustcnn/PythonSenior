# --*--coding:utf-8
# Author:cnn
import socket
import os
import re

"""单进程、单线程非阻塞并发实现web服务器"""
CLRF = "\r\n"
OBJECT_PATH = os.path.dirname(os.path.dirname(__file__))


# print(OBJECT_PATH)

#TODO
class WebServer(object):
    def __init__(self):
        self.ip = "127.0.0.1"
        self.port = 8080
        self.socket_list=list()

    def main(self):
        # 创建socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #将此socket设置成非阻塞
        server_socket.setblocking(False)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定ip
        server_socket.bind((self.ip, self.port))
        # 创建监听
        server_socket.listen()

        while True:
            try:
                # 循环接收客户端连接
                request_socket, request_ip = server_socket.accept()
            except Exception as e:
                print("没有客户端连接.")
            else:
                request_socket.setblocking(False)
                self.socket_list.append(request_socket)
            for client_socket in self.socket_list:
                try:
                    recv_data=client_socket.recv(1024)
                except Exception as rsc:
                    print("没有客户端发送数据.")
                else:
                    recv_data_str=recv_data.decode("utf8")
                    print(recv_data_str)
                    if recv_data:
                        pass
                    else:
                        client_socket.close()
                        self.socket_list.remove(client_socket)

if __name__ == '__main__':
    web_server = WebServer()
    web_server.main()

