import threading 
import socket
import sys
import time


host = ''
port = 9000
locaddr = (host,port) 


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

tello_address = ('192.168.10.1', 8889)

sock.bind(locaddr)

def recv():
    count = 0
    while True: 
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\nExit . . .\n')
            break


print ('\r\n\r\nTello Commander.\r\n')

print ('\'end\' to quit\r\n')


#recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()

def check_custom_msg(msg):
    if( msg == 'square-movement' ):
        print('Going square')
        sock.sendto('takeoff', tello_address)
        for i in range(4):
            sock.sendto('forward 100', tello_address)
            sock.sendto('cw 90', tello_address)
        sock.sendto('land', tello_address)
        return True

while True: 

    try:
        msg = input("")
        custom = check_custom_msg(msg)

        if custom:
            print('custom command')
            break

        if not msg:
            break  

        if 'end' in msg:
            print ('...')
            sock.close()  
            break

        # Send data
        msg = msg.encode(encoding="utf-8") 
        sent = sock.sendto(msg, tello_address)
    except KeyboardInterrupt:
        print ('\n . . .\n')
        sock.close()  
        break
