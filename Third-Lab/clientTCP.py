from socket import *

serverName = "localhost"
serverPort = 12000

#sock_stream indicates a tcp connection
clientSocket = socket(AF_INET, SOCK_STREAM)
socket = (serverName, serverPort)
#connects to the server by passing as parameter the combination of host name and port
clientSocket.connect(socket)


message = input("insert something ")
clientSocket.send(message.encode("utf-8"))

modifiedMessage = clientSocket.recv(1024)
print("from the server: ", modifiedMessage.decode("utf-8"))

clientSocket.close()
