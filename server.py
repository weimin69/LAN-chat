import socket
import threading

clients = []

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg, client)

        except:
            clients.remove(client)
            client.close()
            break
def broadcast(msg, sender):
    for client in clients:
        if client != sender:
            client.send(msg)

sever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sever.bind(("0.0.0.0", 9999))
sever.listen()

print("服务器启动")

while  True:
    client, addr = sever.accept()
    print("用户连接: {addr}")

    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()
