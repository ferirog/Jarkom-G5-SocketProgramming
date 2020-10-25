import socket

HEADER = 64
PORT = 16142
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = '54.174.236.0'
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)
print(client.recv(2048).decode(FORMAT))

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

    print(client.recv(2048).decode(FORMAT))

print("Hello! insert the array to sort:")

the_input = input()
send(the_input)

print(client.recv(2048).decode(FORMAT))
print(client.recv(2048).decode(FORMAT))
send(DISCONNECT_MESSAGE)
print(client.recv(2048).decode(FORMAT))