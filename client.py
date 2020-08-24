import socket

HEADER = 128
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
# SERVER = "193.17.28.21" # puplic school IP
SERVER = "172.22.242.247" # local school IP
# SERVER = "192.168.178.31" # local home IP
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
connected = True


def send_message(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    msg_length_send = str(msg_length).encode(FORMAT)
    msg_length_send_padded = msg_length_send + b' ' * (HEADER - len(msg_length_send))
    client.send(msg_length_send_padded)
    client.send(message)


while connected:
    msg = input()
    send_message(msg)
    if msg == DISCONNECT_MESSAGE:
        connected = False
