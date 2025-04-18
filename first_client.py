# import socket

# HOST = '127.0.0.1'
# PORT = 1234
# address = (HOST,PORT)
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# client_socket.connect(address)
# print(f'client connected to {HOST}:{PORT}')


# client_socket.sendall('Hello Server!!!'.encode('utf-8'))

# while True:
#     try:
#         data = client_socket.recv(1024)
#         if not data:
#             break
#     except ConnectionResetError:
#         break

# client_socket.close()
# print('connection is closed')



import socket

HOST = '127.0.0.1'
PORT = 1234

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client_socket.connect((HOST,PORT))
print(f"The client is connected to server{HOST}:{PORT}")

client_socket.sendall("client anwser:hello server!".encode('utf-8'))

while True:
    try:
        data = client_socket.recv(1024)
        print(data.decode())
        if not data :
            break

    except ConnectionResetError:
        break    

client_socket.close()
print('connection is closed')    