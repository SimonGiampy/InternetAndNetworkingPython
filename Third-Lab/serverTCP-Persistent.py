from socket import *

serverPort = 12000
#sock_stream indicates a tcp connection
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
#with this line it says that can accept 1 client, the others will be put in queue, and the last client will be refused
serverSocket.listen(3)
print("server is ready to receive data")

while 1: #infinite loop that listens for any response
    (connectionSocket, clientAddress) = serverSocket.accept()
    print("connected to: ", clientAddress)

    while True:
        #1024 are the bytes that the server is available to receive, and TCP doesn't include the address too
        sentence = connectionSocket.recv(1024)
        sentence = sentence.decode("utf-8").upper().encode("utf-8") #formatting received data

        connectionSocket.send(sentence)

    connectionSocket.close()