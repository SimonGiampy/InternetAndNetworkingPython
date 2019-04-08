from socket import *

serverName = "localhost"
serverPort = 12000

#sock_stream indicates a tcp connection
clientSocket = socket(AF_INET, SOCK_STREAM)
socket = (serverName, serverPort)
clientSocket.connect(socket)

while True:
    message = input("insert something ")
    clientSocket.send(message.encode("utf-8"))

    if message == '.':
        break

    modifiedMessage = clientSocket.recv(1024)
    print(modifiedMessage.decode("utf-8"))

clientSocket.close()
