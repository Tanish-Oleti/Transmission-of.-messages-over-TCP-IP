import socket
import threading
import time

HEADER = 64
# choosing a port to communicate ,better to use a port which is not used for other purposes
PORT = 5050
# getting ip address of host
SERVER = "0.0.0.0"  # socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# INET means using ipv4 addresses
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# this makes sure that when a client wants to communicate and it gives the address it is referred to this socket
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            print(f"[{addr}] {msg}")
            conn.send("Msg received".encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        
        conn, addr = server.accept()
        print(conn)
        print(server)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # threading makes sure that multiple clients can be connected to server at same time
        # printing active threads
        # as the start thread is always active we will subtrract one thread fromm all
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print("[STARTING] server is starting...")
start()
