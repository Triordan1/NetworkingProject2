from socket import *
import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        print("Starting {}".format(self.name))
        send_message(self.name)
        print("Exiting {}".format(self.name))

def send_message(thread_name):
    serverName = 'localhost'
    serverPort = 12000
    # Create a TCP connection
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    print("Sent {}".format(thread_name))
    
    # Send message and retrieve a response
    clientSocket.send(thread_name.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server:', modifiedSentence.decode())
    clientSocket.close()

thread1 = MyThread("Client X: Alice")
thread2 = MyThread("Client Y: Bob")

thread1.start()
thread2.start()