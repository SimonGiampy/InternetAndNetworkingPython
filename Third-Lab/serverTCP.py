from socket import *

serverPort = 12000
#sock_stream indicates a tcp connection
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("server is ready to receive data")

while 1: #infinite loop that listens for any response
    (connectionSocket, clientAddress) = serverSocket.accept()
    print("connected to: ", clientAddress)

    #1024 are the bytes that the server is available to receive, and TCP doesn't include the address too
    sentence = connectionSocket.recv(1024)
    sentence = sentence.decode("utf-8").upper().encode("utf-8") #formatting received data

    connectionSocket.send(sentence)

    connectionSocket.close()