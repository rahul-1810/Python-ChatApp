import socket
import threading 
import os

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip = input("\n\t\tEnter Your IP : ")
port = 3030

s.bind( (ip,port) )

sip = input("\n\t\tEnter Server IP : ")
sport = 4040

print()

def send():

    while True:
        os.system('color b')
        msg = input('\n\n').encode()
        s.sendto(msg,(sip,sport))
        if msg.decode() == "exit":
            os._exit(1)
        
def recv():
    while True:
        os.system('color a')
        msg = s.recvfrom(1024)
        if msg[0].decode() == "bye":
            os._exit(1)
        
        print('\n\tReceived -> ' + msg[0].decode())
    



t1 = threading.Thread(target=send)
t2 = threading.Thread(target=recv)

t1.start()
t2.start()
