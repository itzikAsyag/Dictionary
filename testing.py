import ClientClass

client = ClientClass.Client_Class("Itzik")
client.Connect()
dict = client.getDicionary()
dict['1'] = "Eitan"
dict['0'] = "Itzik"
print(dict)
client.Disconnect()
