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


if __name__ == "__main__":
    pass

    chat = chatter('192.168.45.52',50007,50008)
    chat.startChat()

    # send messages
    # equiv: echo 'xxx' | nc -u -p 50002 x.x.x.x 50001

    #"""