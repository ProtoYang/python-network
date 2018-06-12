import socket


def send_file_2_client(new_client_socket, client_address):

    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载的文件是： %s" % (str(client_address), file_name))

    file_content = None
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()

    except Exception as ret:

        print("没有此文件(%s)" % file_name)
    new_client_socket.send(file_content)


def main():
    # 创建套接字
    tcp_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 绑定本地信息
    tcp_socket_server.bind(("", 7788))
    # 设置套接字为监听链接请求，并得到客户端信息
    tcp_socket_server.listen(128)
    new_client_socket, client_address = tcp_socket_server.accept()

    # 发送文件数据给客户端
    send_file_2_client(new_client_socket, client_address)


if __name__ == "__main__":
    main()