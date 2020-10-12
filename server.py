import socket
import threading

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR =(SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"
print(f"Server : {SERVER}, Port : {PORT}")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"{addr} connected")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT:
                connected=False
            print(f"{addr} : {msg}")
            conn.send(f"Message [{msg}]  receievd".encode(FORMAT))
    #conn.close()

def start():
    print(f"Server is listening on {SERVER}")
    server.listen()
    conn, addr = server.accept()
    thread = threading.Thread(target=handle_client, args=(conn, addr))
    thread.start()
    print(f"Active connections: {threading.active_count()-1}")



print("Starting server....")
start()