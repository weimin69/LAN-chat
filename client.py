import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sever_ip = input("输入服务器IP")

client.connect((sever_ip,9999))

def receive():
    while True:
        try:
            msg = client.recv(1024)
            print(msg.decode())
        except:
            print("连接断开")
            break

threading.Thread(target=receive).start()

while True:
    msg = input()
    client.send(msg.encode())
