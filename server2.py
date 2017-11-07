import socket
import sys

_updateHeader = 7
_updteOperationHeader = 4
_updateFullHeader = 11
_closeHeader = 6

# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 12345)
print >>sys.stderr, 'starting up on %s port %s' % server_address
server.bind(server_address)

# Listen for incoming connections
server.listen(5)

my_dict = {}

while True:
    c, addr = server.accept()  # Establish connection with client.
    print 'Got connection from', addr
    data = c.recv(1024)
    array = data.split("\n")
    for word in array:
        if word[:_updateHeader] == 'update:':
            numIndex = 0 ;
            for i in range(_updateFullHeader , len(data)):
                if word[i] == ',':
                    numIndex = i-_updateFullHeader # 11 because is the "update:" string + op("del:"/"add:") string
                    break
            key = word[_updateFullHeader:_updateFullHeader+numIndex]
            value = word[(_updateFullHeader+numIndex)+1: len(data)]
            if word[_updateHeader:_updateFullHeader]  == "add:":
                my_dict[key] = value
            else:
                del my_dict[key]
            print(my_dict)
        elif word[:_closeHeader] == "close:":
            server.shutdown
            print("Bye Bye")
