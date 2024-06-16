import socket
import time
HEADER = 64
PORT = 5050
FORMAT = "utf-8"
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "0.0.0.0"  # socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
CLIENT = "0.0.0.80"
ADDR1 = (CLIENT, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.bind(ADDR1)
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("hello world ,how are u")
send(DISCONNECT_MESSAGE)
send("hello nonsense how are u doing")
send(DISCONNECT_MESSAGE)
count=0

while True:
    time.sleep(1)
    if count<10:
        HEADER = 64
        PORT = 5050
        FORMAT = "utf-8"
        DISCONNECT_MESSAGE = "!DISCONNECT"
        SERVER = "0.0.0.0"  # socket.gethostbyname(socket.gethostname())
        ADDR = (SERVER, PORT)
        CLIENT = "0.0.0.80"
        ADDR1 = (CLIENT, PORT)
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # client.bind(ADDR1)
        client.connect(ADDR)

        count+=1
        c=str(count)
        print(c)
        send(c)
        send(DISCONNECT_MESSAGE)
        print("hello world")
        
    else:
        break
