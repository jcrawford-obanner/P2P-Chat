# first of all import the socket library
import socket            
 
status_dict={}
# next create a socket object
s = socket.socket()        
print ("Socket successfully created")
 
# reserve a port on your computer in our
# case it is 12345 but it can be anything
port = 12345               
 
# Next bind to the port

s.bind(('', port))        
print ("socket binded to %s" %(port))
 
# put the socket into listening mode
s.listen(5)    
print ("socket is listening")           
 
# a forever loop until we interrupt it or
# an error occurs

c, addr = s.accept()    
print ('Got connection from', addr )
status_dict[addr[0]]= "online"
print("status: ", status_dict)

while True:
 
# Establish connection with client.
  msg = c.recv(1024).decode()
  print(msg)
  if(msg == "goodbye"):
    status_dict[addr[0]]= "offline"
    print("status: ", status_dict)
    c.close()
    break
 