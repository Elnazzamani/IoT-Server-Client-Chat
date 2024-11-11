#Autor: Elnaz zamani

import socket as so
import threading as th 

Host = '0.0.0.0'
Port = 5000

def manageClient(client_socket):
    while True:
            incomingMessage = client_socket.recv(1024).decode('utf-8')
            if incomingMessage:
                print(" ClientMessage :" ,  incomingMessage)
            else:
                break

    client_socket.close()
    print("Client is not available!!")

def configure_server():
    socketListener = so.socket( so.AF_INET , so.SOCK_STREAM )
    socketListener.bind((Host , Port ))
    socketListener.listen(5)

    client_socket, address = socketListener.accept()
    thread = th.Thread( target=manageClient , args=( client_socket ,))
    thread.start()

    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

configure_server()

