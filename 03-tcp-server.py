from socket import *


def main():
    # 1.创建套接字,绑定
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.bind(("", 60000))
    # 2.设置套接字为接收模式
    tcp_server_socket.listen(128)
    while True:
        # 3.监听端口，存链接的套接字
        print("等待接受数据")
        client_socket, client_addr = tcp_server_socket.accept()
        # 4.接受客户端请求
        print("一个客户链接成功：%s" % str(client_addr))
        while True:
            recv_data = client_socket.recv(1024)
            if not recv_data:
                break
            print("客户:" + recv_data.decode("utf-8"))
            # 5.回复
            client_socket.send("收到".encode("gbk"))
        # 6.关闭两个套接字
        print("服务完毕")
        client_socket.close()

    print("客户端关闭")
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
