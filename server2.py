import socket
import sys
from time import sleep

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
c, addr = server.accept()  # Establish connection with client.
print 'Got connection from', addr

while True:
    try:
        data = c.recv(1024)
    except socket.timeout, e:
        err = e.args[0]
        # this next if/else is a bit redundant, but illustrates how the
        # timeout exception is setup
        if err == 'timed out':
            sleep(1)
            print 'recv timed out, retry later'
            continue
        else:
            print e
            sys.exit(1)
    except socket.error, e:
        # Something else happened, handle error, exit, etc.
        print e
        sys.exit(1)
    else:
        if len(data) == 0:
            print 'orderly shutdown on server end'
            sys.exit(0)
        else:
                if data[:_updateHeader] == 'update:':
                    if data[_updateHeader:_updateFullHeader] == "ext:":
                        server.shutdown
                        print("Bye Bye")
                        sys.exit()
                    else:
                        numIndex = 0 ;
                        for i in range(_updateFullHeader , len(data)):
                            if data[i] == ',':
                                numIndex = i-_updateFullHeader # 11 because is the "update:" string + op("del:"/"add:") string
                                break
                        key = data[_updateFullHeader:_updateFullHeader+numIndex]
                        if data[_updateHeader:_updateFullHeader]  == "add:":
                            c.send("recive!")
                            print("add")
                            value = data[(_updateFullHeader + numIndex) + 1: len(data)]
                            my_dict[key] = value
                        elif data[_updateHeader:_updateFullHeader]  == "del:":
                            c.send("recive!")
                            print("delete")
                            del my_dict[key]
