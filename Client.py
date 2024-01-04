from socket import *
import threading
import json

f = open("Very_Basic_Auth_Passwd.txt")
details = json.loads(f.read())

servername = 'localhost'
serverport = details["port"]
clientsocket = socket(AF_INET,SOCK_DGRAM)

authed = 0

while(authed == 0):
    ps = input("Enter Auth pass to enter: ")
    if(ps == details["passwd"]):
        authed = 1

if(authed == 1):
    proceed = "0"
    while(proceed=="0"):
        a = input("Enter your name in room: ")
        clientsocket.sendto(("1+"+a.lower()).encode(),(servername,serverport))
        msg, addr = clientsocket.recvfrom(2048)
        proceed = msg.decode()
        if(proceed=="0"):
            print("Name already taken!!")

    print("Name accepted!!")
    quit1=0
    quit2=0

    def recieve():
        global quit1
        while(quit1==0):
            try:
                msg, addr = clientsocket.recvfrom(2048)
                print(msg.decode())
            except:
                break
    def send():
        global quit1
        global quit2
        while(quit2==0):
            sendmsg = input()
            if(sendmsg=="q"):
                quit1=1
                quit2=1
                clientsocket.sendto(("1-"+a.lower()).encode(),(servername,serverport))
                clientsocket.close()
            else:
                clientsocket.sendto((a+": "+sendmsg).encode(),(servername,serverport))

    x = threading.Thread(target=recieve)
    y = threading.Thread(target=send)
    x.start()
    y.start()
    x.join()
    y.join()