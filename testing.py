import ClientClass
from time import sleep

client = ClientClass.Client_Class("Itzik")
client.Connect()
dict = client.getDicionary()
dict['1'] = "Eitan"
dict['0'] = "Itzik"
print(dict)
del dict['0']
print(dict)
client.Disconnect()
