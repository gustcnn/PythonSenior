# --*--coding:utf-8
# Author:cnn
import socket
"""返回客户端固定的页面"""
CLRF = "\r\n"


def service_client(client_socket):
    # 接收客户端发送的请求
    recv_client_data = client_socket.recv(1024)
    print(recv_client_data.decode())
    #if recv_client_data:
    # 响应头
    response = "HTTP/1.1 200 OK" + CLRF
    # 设置响应头的Content-Type为utf8,则浏览器按照utf8解析
    response += "Content-Type:text/html;charset=utf-8" + CLRF
    # 空行
    response += CLRF
    # body
    response += "<h1>少不看三国</h1>" + CLRF
    # 返回响应
    # client_socket.send(response.encode("gb2312"))
    client_socket.send(response.encode("utf8"))
    # else:
    # 关闭套接字
    client_socket.close()


def main():
    # 创建socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #保证服务器端先关闭,也不会出现端口被占用
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    # 绑定ip
    server_socket.bind(("127.0.0.1", 8080))
    print("服务器端已启动,等待客户端连接.")
    # 监听
    server_socket.listen()
    try:
        while True:
            # 接收客户端连接
            client_socket, client_address = server_socket.accept()
            # 为客户端服务
            service_client(client_socket)
    finally:
        server_socket.close()


if __name__ == '__main__':
    main()
