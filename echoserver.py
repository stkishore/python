import socket
UDP_IP_ADDRESS="10.1.24.119"
UDP_PORT_NUMBER=6723
serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS,UDP_PORT_NUMBER))
print("msg receiving")
while True:
  data, addr = serverSock.recvfrom(1024)
  print("Message:",data)
  serverSock.sendto(data, addr)
