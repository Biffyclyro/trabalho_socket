import socket
import time

# metodo responsável por enviar a mensagem tcp
def send_msg_tcp(msg):
    with socket.socket() as s:
        s.connect(('localhost', 8090))
        s.send(bytes(msg))
        print(s.recv(1024).decode('utf-8'))

# método responsaǘel por enviar mensagem udp
def send_msg_udp(msg):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto( bytes(msg), ('localhost', 8080))


#classe responsável por simular colheitadeira
class Colheiradeira:
    max_lng = 10
    max_lat = 10

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng
        self.max_lat += lat
        self.max_lng += lng

    def move(self):
        time.sleep(0.5)
        if self.lat < self.max_lat:
            if self.lat % 2 == 0:
                if self.lng < self.max_lng:
                    self.lng += 1
                else:
                    self.lat += 1
            else:
                if self.lng > self.max_lng - 9:
                    self.lng -= 1
                else: 
                    self.lat += 1

        return (self.lat, self.lng)



c = Colheiradeira(0, 0)

while c.lat < c.max_lat:
   send_msg_tcp( c.move())
   #send_msg_udp( c.move())
