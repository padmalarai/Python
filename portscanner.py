import socket

remoteserver=input("Pls enter remote server name or ip for port scanning:")


remoteipaddress= socket.gethostbyname(remoteserver)

for port in range(131,151):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result= sock.connect_ex((remoteipaddress, port))
    if result == 0:
        print("{} is open".format(port))
    else:
        print("{} is closed".format(port))
        
