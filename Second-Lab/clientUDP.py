from socket import *

#simbolic server name (a string or the server address) and port (an integer)
serverName = "localhost"
serverPort = 23402

#sock_dgram indicated UDP protocol. opens a socket
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(5)

#asks for user input
message = input("insert some random words: ")

#tuples are arrays which can't be modified after being assigned
#configures the socket with the server port and name
clientSocket.sendto(message.encode("utf-8"), (serverName, serverPort))

try:
    # 2048 is the buffer size
    # reads the data of the server response from the socket,
    # and memorizes it in a string
    (modifiedMessage, serverAddress) = clientSocket.recvfrom(2048)
    # shows the received string
    print(modifiedMessage.decode("utf-8"))
except timeout:
    print("error found")
#except Exception as ex:
 #   template = "An exception of type {0} occurred. Arguments:\n{1!r}"
  #  message = template.format(type(ex).__name__, ex.args)
   # print(message)
finally:
    clientSocket.close()
