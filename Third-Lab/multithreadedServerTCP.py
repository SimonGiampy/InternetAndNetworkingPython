from socket import *
from threading import Thread

def handler(connectionSocket):
        while True:
            sentence = connectionSocket.recv(1024)
            if sentence.decode("utf-8") == ".":
                break

            connectionSocket.send(sentence.decode("utf-8").upper().encode("utf-8"))
        connectionSocket.close()

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)

while True:
    print("server is ready to receive ")
    (newSocket, address) = serverSocket.accept()
    thread = Thread(target=handler, args=(newSocket,))
    thread.start()
