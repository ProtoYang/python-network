import socket


def main():
    # 创建一个套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定一个本地端口
    localaddr = ("", 8080)
    udp_socket.bind(localaddr)
    while True:
        # 接受数据
        recv_data = udp_socket.recvfrom(2048)

        print(recv_data[0].decode("gbk"))
        print(recv_data[1][0])
        send_data = input("请输入要发送的数据")
        if send_data == "q":
            break

        # 可以使用套接字收发数据
        udp_socket.sendto(send_data.encode("gbk"), ("192.168.1.148", 8080))
    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()

