import socket
host = 'localhost'
data_payload = 2048
port = 9900
# Create a UDP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_address = (host, port)
print ("Connecting to %s port %s" % server_address)
try:
# Send data
message = input("Enter your message:")
print ("Sending %s" % message)
sent = sock.sendto(message.encode('utf-8'), server_address)
# Receive response
data, server = sock.recvfrom(data_payload)
print("----------At server-------------")
print ("received %s" % data)
print("---------------------------------")
finally:
print ("Closing connection to the server")
sock.close()
