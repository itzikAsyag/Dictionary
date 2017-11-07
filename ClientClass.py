import Dictio
import socket
import sys
import threading

class Client_Class :

    def __init__(self , username): #initialize , getting username from user
        self._name = username
        self._flag = True
        self._cv = threading.Condition()

    def Connect(self): # create connection to server with host and ip variables from user
        HOST = input("\nNet Send Server Public IP: ")
        PORT = int(input("\nNet Send Server Port: "))
        try:
            self._server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self._server.connect((HOST, PORT))
            print("Connected to server:", HOST,)
            return self._server
        except IOError:
            print("\n\n\a\t\tUndefined Connection Error Encountered")
            input("Press Enter  to exit, then restart the script")
            sys.exit()

    ''' * send message that write the user in prompt
    * i added the string "msg: " that when the 
      server read that he know that is a message and not update'''
    def SendMessage(self):
        if self._server is not None:
            msg = input("\nyour Message : ")
            self._server.send("msg: "+self._name + " : " + msg)
        else:
            print("\n there is no server")

    def getDicionary(self): #create dictionary if is not exists
        if not hasattr(self , '_dict'):
            self._dict = Dictio.LowerDict(self)
        return self._dict

    def Disconnect(self): #disconnect from server
        if self._server is not None:
            self.SendUpdate("ext")


    def SendUpdate(self , op , key=None, value=None): #when the dictionary is changet this method will call
        if hasattr(self, '_server') and hasattr(self, '_dict'):
            self._cv.acquire
            if op == "del":
                self._server.send("update:" + op + ": " + key + ",\n")
            elif op == "ext":
                self._server.send("update:" + op + ",\n")
                self._server.shutdown
                return
            else:
                self._server.send("update:"+op+": " + key+","+value+"\n")
            self._flag = False
            while not self._flag:
                data = self._server.recv(1024)
                print(data)
                if data == "recive!":
                    self._flag = True
                    self._cv.release
        else:
            print("\n there is no server")

