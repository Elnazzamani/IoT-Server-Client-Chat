#Autor Elnaz zamani
import socket as so
import threading as th

Host = '127.0.0.1'
Port = 5000


def getMessages(connectionSocket):
    while True:
            incomingMessage = connectionSocket.recv(1024).decode('utf-8')
            if incomingMessage:
                print("Server:", incomingMessage)
            else:
                break

def configure_client():
    connectionSocket = so.socket(so.AF_INET, so.SOCK_STREAM)
    while True:
            connectionSocket.connect((Host , Port))
            print("Connected to server")
            break
    thread = th.Thread( target = getMessages , args = (connectionSocket,) )
    thread.start()

    while True:
        your_message = input()
        connectionSocket.send(your_message.encode('utf-8'))

configure_client()
