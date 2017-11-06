import select
import socket
import sys
import dictionaryObserver
import json
import Queue

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
    str = data[0:6]
    if data[0:6] == 'update:':
        numIndex = 0 ;
        for i in range(0 , len(data)):
            if data[i] == ',':
                numIndex = i-10 # 10 because is the "update:" string + op("del"/"add") string
        key = data[10:10+numIndex]
        value = data[10+numIndex: len(data)]
        if data[6:9]  == "add":
            my_dict[key] = value
        else:
            del my_dict[key]
        print(my_dict)
    elif data[0:5] == "close:":
        server.shutdown
        print("Bye Bye")
