import socket

HOST = '127.0.0.1'
PORT = 5555


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((HOST, PORT))
sock.listen(10)

while True:
    client_socket, address = sock.accept()
    print(f'connection from {address}...')
    msg = client_socket.recv(1024)
    print(msg)