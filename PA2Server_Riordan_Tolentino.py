'''

Multithreading is needed on the server program so that the retrieving of 

client messages is done synchronously. Without it, the server would always say that the

first connection established sent the first message.

'''

from socket import *

import threading

​

serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('',serverPort))

serverSocket.listen(2)

​

messages = []

client_sockets = []

print("The server is ready to receive")

​

# Omits the initial "Client" string from message

def split_string(message):

     return message.split(" ", 1)[1]

​

def receive_thread_message(client_socket):

     global messages

     messages.append(client_socket.recv(1024).decode())

​

# Keep server open

while True:

     # Listen for TCP packets

     while len(client_sockets) < 2:

          client_socket, addr = serverSocket.accept()

          client_sockets.append(client_socket)

     

     # Start threads to receive message for each socket 

     thread1 = threading.Thread(target=receive_thread_message,args=(client_sockets[0],))

     thread2 = threading.Thread(target=receive_thread_message,args=(client_sockets[1],))

     thread1.start()

     thread2.start()

     thread1.join()

     thread2.join()

​

     # Send acknowledgment to both sockets

     for i in range(2):

          client_sockets[i].send("{} received before {}".format(messages[0], messages[1]).encode())

          client_sockets[i].close()

     print("Sent acknowledgment to both {} and {}".format(split_string(messages[0]), split_string(messages[1])))

     client_sockets.clear()

     messages.clear()

     

serverSocket.close()

