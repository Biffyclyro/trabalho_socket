import socket
from threading import Thread


def tcp_listener():
    with socket.create_server(('localhost', 8090)) as ss:
        while True:
            conn, addr = ss.accept()
            with conn:
                print('conectado com', addr)
                print( tuple(conn.recv(1024)) )
    

def udp_listener():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as ss:
        ss.bind(('localhost', 8080))
        while True:
            msg, addr = ss.recvfrom(1024)
            print(f'{tuple(msg)} recebido de {addr}')


def main():
    tcp_server = Thread(target=tcp_listener)
    udp_server = Thread(target=udp_listener)

    tcp_server.start()
    udp_server.start()

    tcp_server.join()
    udp_server.join()


if __name__ == '__main__':
    main()







