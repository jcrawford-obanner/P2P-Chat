import socket
import sys
import threading



#tcpSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#CONNECT TO SERVER
s = socket.socket()
port = 12345
s.connect((ip,port))


#PROMPT FOR USER TO ENTER PEER DETAILS
ip = ''
sport = 50005
dport = 50004


#ip, sport, dport = data.split(' ')
#sport = int(sport)
#dport = int(dport)

print('\ngot peer')
print('  ip:          {}'.format(ip))
print('  source port: {}'.format(sport))
print('  dest port:   {}\n'.format(dport))

# punch hole
# equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
print('punching hole')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.sendto(b'0', (ip, dport))

print('ready to exchange messages\n')

# listen for
# equiv: nc -u -l 50001
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind(('0.0.0.0', sport))

    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')

listener = threading.Thread(target=listen, daemon=True);
listener.start()

# send messages
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', dport))

while True:
    msg = input('> ')
    s.sendto(msg.encode(), ('192.168.1.158',port))
    if(msg=='goodbye'):
        break
    