from dictionaryObserver import dict_observer
import socket
import sys
import json

class Client_Class :

    def __init__(self , username): #initialize , getting username from user
        self._name = username

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
            value = {'-1':'Zara'}
            self._dict = dict_observer(value,self.SendUpdate())
        return self._dict

    def Disconnect(self): #disconnect from server
        if self._server is not None:
            self._server.send("close:")
            self._server.close(self)
            self._server = None

    def SendUpdate(self): #when the dictionary is changet this method will call
        if hasattr(self, '_server') and hasattr(self, '_dict'):
            if len(self._dict) == 1:
                data_string = json.dumps(self._dict)  # data serialized
                self._server.send("dict: " + data_string)
            else:
                msg = input("\nyour update : ")
                self._server.send("update: "+self._name + " : " + msg)
        else:
            print("\n there is no server")

