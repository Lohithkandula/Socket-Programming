import socket
host = 'localhost'
port = 9900
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the server
server_address = (host, port)
print("Connecting to %s port %s" % server_address)
s.connect(server_address)
# Send data
try:
message = input("Write a message:")
print("Sending %s" % message)
s.sendall(message.encode('utf-8'))
# Look for the response
amount_received = 0
amount_expected = len(message)
while amount_received < amount_expected:
data = s.recv(16)
amount_received += len(data)
print("-------------at server-------------")
print("Received: %s" % data)
print("----------------------------------")
except socket.error as e:
print("Socket error: %s" % str(e))
except Exception as e:
print("Other exception: %s" % str(e))
finally:
print("Closing connection to the server")
s.close()
