import socket
import sys


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8008)

s.connect(server_address)

try:
    # Send data
    message = 'This is the message.  It will be repeated.'
    print >>sys.stderr, 'sending "%s"' % message
    s.sendall(message)

    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    # while there is data that are to be proceeded
    while amount_received < amount_expected:
        data = s.recv(1024)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data
        

finally:
    print >>sys.stderr, 'closing socket'
    s.close()