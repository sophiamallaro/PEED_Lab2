import socket

UDP_IP = '0.0.0.0'  # 0.0.0.0 IPv4
UDP_PORT = 5005

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = s.recvfrom(1024)  # 1024 bytes buffer
    print('received message', data)
