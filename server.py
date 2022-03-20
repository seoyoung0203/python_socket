from socket import *

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', 3001))
serverSocket.listen(1)
print("연결대기중...")

connectionSocket, addr = serverSocket.accept()
print('연결 주소: ', str(addr))

while True:
    data = connectionSocket.recv(1024)
    print('받은 메세지: ', data.decode('utf-8'))
    msg = input('server >>>')
    connectionSocket.send(msg.encode('utf-8'))