from socket import *
import threading
import time

def send(sock):
    while True:
        msg = input('client >>>')
        sock.send(msg.encode('utf-8'))

def receive(sock):
    while True:
        data = sock.recv(1024)
        print('받은 메세지: ', data.decode('utf-8'))

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 3001))
print('연결')

sender = threading.Thread(target=send, args=(clientSocket, ))
receiver = threading.Thread(target=receive, args=(clientSocket, ))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass