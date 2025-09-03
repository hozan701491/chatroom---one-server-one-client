import socket

while True:
    HOST = '127.0.0.1'
    PORT = 1400
    print(f'server is lestning of {HOST} : {PORT}')
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_socket.bind((HOST,PORT))

    server_socket.listen(1)
    client_socket,client_address = server_socket.accept()
    print(f'accepted a new connection from{client_address}')


    while True :
        try :
            data = client_socket.recv(1024)

            if not data :
                break
            
            if data :
                print(data.decode()) 
            
       
             
        except ConnectionResetError:
            break
        client_socket.send(" server anwser : hello client!!!".encode())
       
    client_socket.close()
    print(f'connection with {client_address} closed!')

    server_socket.close()
    print("The sever is shut down!!")
            
    
# HOST = '127.0.0.1'
# PORT = 1234
# print(f'server is lestning of {HOST} : {PORT}')
# server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# server_socket.bind((HOST,PORT))

# server_socket.listen(1)
# client_socket,client_address = server_socket.accept()
# print(f'accepted a new connection from{client_address}')


# while True :
#     try :
#         data = client_socket.recv(1024)

#         if not data :
#             break
            
#         if data :
#             print(data.decode()) 
            
       
             
#     except ConnectionResetError:
#         break
#     client_socket.send(" server anwser : hello client!!!".encode())
       
# client_socket.close()
# print(f'connection with {client_address} closed!')

# server_socket.close()

# print("The sever is shut down!!")
