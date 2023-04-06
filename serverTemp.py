# first of all import the socket library
import socket            
import threading
 
status_dict={}
 
socket_dict={}
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12382
 
# Next bind to the port

s.bind(('', port))    
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)            
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
#s.listen(5)    
#print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs

#c, addr = s.accept()    
#print ('Got connection from', addr )
#status_dict[addr]= "online"
#print("status: ", status_dict)

def listen():
    #while True:
        #s.close()
        s.listen(5)    
        print ("socket is listening")           
        
        # a forever loop until we interrupt it or
        # an error occurs

        c, addr = s.accept() 
        c.sendto(b'ready',addr)
        #c, addr = s.recvfrom(128)
        print ('Got connection from', addr )
        status_dict[addr]= "online"
        print("status: ", status_dict)

        #if len(status_dict) >=2:
            #break

#listener = threading.Thread(target=listen, daemon=True);
#listener.start()

while True:
        #s.close()
        s.listen(5)    
        print ("socket is listening")           
        
        # a forever loop until we interrupt it or
        # an error occurs
        c, addr = s.accept()
        #try: 
        c.sendto(b'ready',addr)
        #c, addr = s.recvfrom(128)
        print ('Got connection from', addr )
        status_dict[addr]= "online"
        socket_dict[addr] = c
        print("status: ", status_dict)
        #except BrokenPipeError:
        #     print('l')
            #s.close()

        if len(status_dict) >=2:
            break
while True:
    if len(status_dict) >=2:
        keys = list(status_dict.keys())
        c1 = keys[0]
        c1_addr, c1_port = c1
        c2 = keys[1]
        c2_addr, c2_port = c2


        print('{} {} {}'.format(c1_addr, c1_port, 50002))
        socket_dict[keys[1]].sendto('{} {} {}'.format(c1_addr, c1_port, 50055).encode(), c2)
        socket_dict[keys[0]].sendto('{} {} {}'.format(c2_addr, c2_port, 50003).encode(), c1)
        break
"""
# Establish connection with client.
  msg = c.recv(1024).decode()
  print(msg)
  if(msg == "goodbye"):
    status_dict[addr[0]]= "offline"
    print("status: ", status_dict)
    c.close()
    break
"""