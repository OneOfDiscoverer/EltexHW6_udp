import socket

UDPServersocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServersocket.bind(("192.168.0.134", 8090))

while(True):
    sz = UDPServersocket.recvfrom(108)
    message = sz[0]
    address = sz[1]

    clientMsg = "Message from client:{}".format(message)
    clientIP = "Client IP address:{}".format(address)
    print("%s",clientMsg)
    print(clientIP)