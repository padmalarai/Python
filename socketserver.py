import socket

host='127.0.0.1'
port=11834

sock = socket.socket()
sock.bind((host,port)) # bind port in IP address
sock.listen(3)

while True:
    c,addr = sock.accept()
    c.send(b"Thank u conenct with socket server") #c is client information
    print("request from {}".format(addr))
    c.close()

    
    
