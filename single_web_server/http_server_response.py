# --*--coding:utf-8
# Author:cnn
import socket
import os
import re

"""返回客户端请求的页面"""
CLRF = "\r\n"
ip, port = ("127.0.0.1", 8080)
object_path = os.path.dirname(os.path.dirname(__file__))
print(object_path)


def service_client(client_socket):
    """处理请求"""
    # 接收客户端请求
    recv_data = client_socket.recv(1024)
    #解码
    recv_data_str = recv_data.decode("utf8")
    print(recv_data.decode("utf8"))
    # 按照行分割请求内容
    recv_data_list = recv_data_str.splitlines()
    # print(recv_data_list)
    #根据正则匹配GET /login.html HTTP/1.1 中的/login.html
    re_str = r"[^/]+(/[^ ]*)"#不是/的一个或者任意多个字符+/+不是空格的0,1,多个字符
    result = re.match(re_str, recv_data_list[0])
    # print(result)
    file_name = None
    if result:
        file_name = result.group(1)
        if file_name=="/":
            file_name="/index.html"
        #print("*" * 20, file_name)
    # print(type(recv_data_str))

    try:
        file = open(object_path + "/htmls" + file_name, "rb")
    except:
        # 响应头
        response = "HTTP/1.1 404 NOT FOUND" + CLRF
        response += "Content-Type:text/html;charset=utf-8" + CLRF
        response += CLRF
        response+="您要访问的页面不存在."
        # 向客户端发送响应头
        client_socket.send(response.encode("utf8"))
    else:
        # 响应头
        response = "HTTP/1.1 200 OK" + CLRF
        response += "Content-Type:text/html;charset=utf-8" + CLRF
        response += CLRF
        # 向客户端发送响应头
        client_socket.send(response.encode("utf8"))
        # 获得html内容
        content = file.read()
        file.close()
        # 发送body
        client_socket.send(content)
    client_socket.close()


def main():
    # 创建套接字
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # 绑定ip
    server_socket.bind((ip, port))
    # 创建监听
    server_socket.listen()
    print("server starting up...")
    try:
        while True:
            # 循环接收客户端连接
            client_socket, client_ip = server_socket.accept()
            # 为客户端提供服务
            service_client(client_socket)
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
