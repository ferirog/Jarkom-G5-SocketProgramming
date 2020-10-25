import socket 
import threading

HEADER = 64
PORT1 = 16142
SERVER = '172.31.26.134'
ADDR = (SERVER, PORT1)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    dash = "-"
    space = " "
    active = "active"
    conn.send(SERVER.encode(FORMAT)+dash.encode(FORMAT)+str(PORT1).encode(FORMAT)+space.encode(FORMAT)+active.encode(FORMAT))

    connected = True
    running = "running"
    conn.send(running.encode(FORMAT))
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                break 
            array = msg.split(" ")
            array.sort()
            string_sortedarray = ' '.join([str(elem) for elem in array]) 

            print(f"[{addr}] {array}")
            conn.send(string_sortedarray.encode(FORMAT))
            finished = "task finished"
            conn.send(finished.encode(FORMAT))

            
    conn.send(SERVER.encode(FORMAT)+dash.encode(FORMAT)+str(PORT1).encode(FORMAT)+space.encode(FORMAT)+DISCONNECT_MESSAGE.encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        print(f"server accept {conn} {addr}")
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")
        my_input = input()
        if my_input == "disconnect":
            break
    server.close()


print("[STARTING] server is starting...")
start()