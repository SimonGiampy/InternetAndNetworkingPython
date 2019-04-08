from socket import *

serverPort = 6789

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(("", serverPort))

print("server is waiting for a message")

while 1:
    message, clientAddress = serverSocket.recvfrom(2048)
    print("client address: ", clientAddress)
    modifiedMessage = message.decode("utf-8").upper().encode("utf-8")

    serverSocket.sendto(modifiedMessage, clientAddress)

