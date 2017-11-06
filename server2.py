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

my_dict = None

while True:
    c, addr = server.accept()  # Establish connection with client.
    print 'Got connection from', addr
    data = c.recv(1024)
    if data == 'hey':
        c.send('Thank you for connecting')
    elif data[0:4] == 'dict:':
        my_dict = json.loads(data)  # data loaded
        print(my_dict)
    elif data[0:6] == 'update:':
        numIndex = 0 ;
        for i in range(0 , len(data)):
            if data[i] == ',':
                numIndex = i-6
        uIndex = data[6:6+numIndex]
        uData = data[6+numIndex: len(data)]
        my_dict[uIndex] = uData
        print(my_dict)
    elif data[0:5] == "close:":
        server.shutdown
        print("Bye Bye")
