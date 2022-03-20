from socket import *
import threading
import time

def send(sock):
    while True:
        msg = input('server >>>')
        sock.send(msg.encode('utf-8'))

def receive(sock):
    while True:
        data = sock.recv(1024)
        print('받은 메세지: ', data.decode('utf-8'))

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 3001))
serverSocket.listen(1)
print("연결대기중...")

connectionSocket, addr = serverSocket.accept()
print('연결 주소: ', str(addr))

sender = threading.Thread(target=send, args=(connectionSocket, ))
receiver = threading.Thread(target=receive, args=(connectionSocket, ))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass