import socket

host='127.0.0.1'
port=11834

sock = socket.socket()
sock.connect((host,port))
    
    
print(sock.recv(1024))
sock.close()
