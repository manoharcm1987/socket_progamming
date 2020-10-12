import socket


HEADER = 64
PORT = 5050
SERVER = "192.168.0.6"
ADDR =(SERVER, PORT)
FORMAT = "utf-8"
DISCONNECT = "!DISCONNECT"
print(f"Server : {SERVER}, Port : {PORT}")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' '*(HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

send_msg("Hello Server!!!")

send_msg(DISCONNECT)