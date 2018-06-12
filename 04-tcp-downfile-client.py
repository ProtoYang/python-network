import socket


def main():
    # 定义套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 设置ip & port
    server_address = ("192.168.1.106", int("7788"))
    print(server_address)
    # 连接服务器
    tcp_socket.connect(server_address)
    # 获取文件名字
    file_name = input("请输入文件名称：")
    # 文件名字发送到服务器
    tcp_socket.send(file_name.encode("gbk"))
    # 保存接收到的数据到一个文件中
    rece_data = tcp_socket.recv(1024)
    if rece_data:
        with open("New" + file_name, "wb") as f:
            f.write(rece_data)

    # 关闭链接
    # tcp_socket.close()


if __name__ == "__main__":
    main()
