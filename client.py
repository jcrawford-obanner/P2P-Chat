import socket
import sys
import threading

#ip = '10.239.137.36'
ip = '10.239.120.132'
sport = 50005
dport = 50004

print('\ngot peer')
print('  ip:          {}'.format(ip))
print('  source port: {}'.format(sport))
print('  dest port:   {}\n'.format(dport))

# punch hole
# equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
print('punching hole')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, sport))
sock.sendto(b'0', (ip, dport))
sock.close()

print('ready to exchange messages\n')
#"""
# listen for
# equiv: nc -u -l 50001
def listen():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ip, sport))

    while True:
        data = sock.recv(1024)
        print('\rpeer: {}\n> '.format(data.decode()), end='')
        if data == 'exit':
            sock.close()
            break

listener = threading.Thread(target=listen, daemon=True);
listener.start()

# send messages
# equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((ip, dport))

while True:
    msg = input('> ')
    sock.sendto(msg.encode(), (ip, sport))
    if msg == 'exit':
        sock.close()
        break

#"""