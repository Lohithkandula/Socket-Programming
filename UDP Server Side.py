import socket
host = 'localhost'
data_payload = 2048
port = 9900
# Create a UDP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# Bind the socket to the port
server_address = (host, port)
print ("Starting up echo server on %s port %s" % server_address)
sock.bind(server_address)
while True:
print ("Waiting to receive message from client")
data, address = sock.recvfrom(data_payload)
print ("received %s bytesfrom %s" % (len(data), address))
print ("Data: %s" %data)
if data:
sent = sock.sendto(data, address)
print("sent %s bytes back to %s" % (sent,address))
