from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 3001))
print('연결')

while True:
    msg = input('client >>>')
    print('msg', msg)
    clientSocket.send(msg.encode('utf-8'))
    print('메세지 전송 완료')

    data = clientSocket.recv(1024)
    print('받은 메세지: ', data.decode('utf-8'))