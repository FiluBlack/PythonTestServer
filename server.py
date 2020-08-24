import socket
import threading

class Server:
    DEFAULT_SERVERIP = socket.gethostbyname(socket.gethostname())
    DEFAULT_PORT = 5050
    DEFAULT_ADDR = (DEFAULT_SERVERIP, DEFAULT_PORT)

    DEFAULT_FORMAT = 'utf-8'
    DEFAULT_HEADER = 128
    DEFAULT_DISCONNECT_MESSAGE = '!DISCONNECT'

    def __init__(self,
                 serverip=DEFAULT_SERVERIP,
                 port=DEFAULT_PORT,
                 format=DEFAULT_FORMAT,
                 header=DEFAULT_HEADER,
                 disconnect_message=DEFAULT_DISCONNECT_MESSAGE):

        self.SERVERIP = serverip
        self.PORT = port
        self.ADDR = (self.SERVERIP, self.PORT)

        self.FORMAT = format
        self.HEADER = header
        self.DISCONNECT_MESSAGE = disconnect_message

    def server_create(self,
                     family=socket.AF_INET,
                     protocoltype=socket.SOCK_STREAM,
                     proto=0,
                     fileno=None):
        server = socket.socket(family, protocoltype, proto, fileno)
        self.server = server
        return server

    def server_bind(self):
        if self.server:
            self.server.bind(self.ADDR)

    def handle_client_connection(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.\n")

        connected = True
        while connected:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False

                print(f"[{addr}] {msg}")

        conn.close()



HEADER = 128
PORT = 5050
# SERVER = "212.53.219.177" # public home IP
# SERVER = "193.17.28.21" # public school IP
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.\n")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False

            print(f"[{addr}] {msg}")

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


print("[STARTING] server is starting...")
start()
