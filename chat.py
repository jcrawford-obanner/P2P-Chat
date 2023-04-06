import socket
import sys
import threading

class chatter:

    
    def __init__(self,ip,sport,dport):
        self.ip = ip
        self.sport = sport
        self.dport = dport

        # punch hole
        # equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
        print('punching hole')

        #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #sock.bind(('0.0.0.0', sport))
        #sock.sendto(b'0', (ip, dport))
        #sock.close()

        print('\ngot peer')
        print('  ip:          {}'.format(ip))
        print('  source port: {}'.format(sport))
        print('  dest port:   {}\n'.format(dport))

        print('ready to exchange messages\n')



    #ip = '10.239.137.36'
    #"""
    # listen for
    # equiv: nc -u -l 50001
    def listen(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', self.sport))

        while True:
            data = sock.recv(1024)
            print('\rpeer: {}\n> '.format(data.decode()), end='')
            if data == 'exit':
                sock.close()
                break

    def talk(self):

        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind(('0.0.0.0', self.dport))

        while True:
            msg = input('> ')
            sock.sendto(msg.encode(), (self.ip, self.sport))
            if msg == 'exit':
                sock.close()
                break

    def startChat(self):
        listener = threading.Thread(target=self.listen, daemon=True)
        speaker = threading.Thread(target=self.talk, daemon=True);
        #speaker.start()
        listener.start()
        #listener.join()
        self.talk()
        #speaker.join()


def main(argv):

    s = socket.socket()
    port = 12382
    #s.bind(('0.0.0.0',50006))
    s.connect(('10.239.82.103',port))
    s.sendto(b'0', ('10.239.82.103',port))
    
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    while True:
        data = s.recv(1024).decode()

        if data.strip() == 'ready':
            print('checked in with server, waiting')
            break

    #PROMPT FOR USER TO ENTER PEER DETAILS
    data = s.recv(1024).decode()
    print(s.getsockname())
    ip, sport, dport = data.split(' ')
    sport = int(sport)
    dport = int(dport)

    print('\ngot peer')
    print('  ip:          {}'.format(ip))
    print('  source port: {}'.format(sport))
    print('  dest port:   {}\n'.format(dport))

    # punch hole
    # equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
    #print('punching hole')

    #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #sock.sendto(b'0', (ip, dport))

    print('ready to exchange messages\n')

    
    chat = chatter(ip,sport,dport)#argv[0],argv[1],argv[2])
    chat.startChat()

    # send messages
    # equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001

    #"""

if __name__ == "__main__":

    main(sys.argv[1:])