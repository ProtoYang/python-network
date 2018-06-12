import socket


def main():
    # 1.创建tcp套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2.链接服务器

    server_ip = input("请输入要链接的服务器ip：")
    server_port = int(input("请输入端口："))
    server_addr = (server_ip, server_port)
    tcp_client_socket.connect(server_addr)
    # 3.发送/接受数据
    while True:
        send_data = input("请输入要发送的内容：")
        if send_data == "q":
            break
        tcp_client_socket.send(send_data.encode("gbk"))
    # 4.关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
