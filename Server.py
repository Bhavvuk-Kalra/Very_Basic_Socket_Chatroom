from socket import *
import json

def send_to_all(a):
    for i in range(len(users)):
        if(users[i]!=a):
            serversocket.sendto((a+" has joined the chatroom!!").encode(),addresses[i])

def send_to_all2(a):
    for i in range(len(users)):
        if(users[i]!=a):
            serversocket.sendto((a+" has left the chatroom!!").encode(),addresses[i])
def send_the_msg(a,m):
    print(m)
    for i in range(len(users)):
        if(users[i]!=a):
            serversocket.sendto(m.encode(),addresses[i])


f = open("Very_Basic_Auth_Passwd.txt")
details = json.loads(f.read())

serverport = details["port"]
serversocket = socket(AF_INET,SOCK_DGRAM)
serversocket.bind(('',serverport))
print("ChatRoom initiated!!")
users = []
addresses = []
while(True):
    msg, clientAddr = serversocket.recvfrom(2048)
    if(msg.decode()[:2]=="1+"):
        if(msg.decode()[2:].lower() not in users):
            users.append(msg.decode()[2:].lower())
            addresses.append(clientAddr)
            print(msg.decode()[2:].lower()," has joined the chatroom!!")
            send_to_all(msg.decode()[2:].lower())
            serversocket.sendto("1".encode(),clientAddr)
        else:
            serversocket.sendto("0".encode(),clientAddr)
    elif(msg.decode()[:2]=="1-"):
        for i in range(len(users)):
            if(users[i]==msg.decode()[2:].lower()):
                torem = i        
        addresses.remove(addresses[torem])
        users.remove(users[torem])
        print(msg.decode()[2:].lower()," has left the chatroom!!")
        send_to_all2(msg.decode()[2:].lower())
    else:
        for i in range(len(addresses)):
            if(addresses[i]==clientAddr):
                torem = i
        send_the_msg(users[torem],msg.decode())
