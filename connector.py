import socket

HOST = '127.0.0.1'
PORT = 4455

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sock.connect((HOST, PORT))

# while True:
#     full_msg = ''
#     new_msg = True
#     while True:
#         msg = sock.recv(16)
#         if new_msg:
#             print(f'msg size: {msg[:10]}')
#             msglen = int(msg[:10])
#             new_msg = False
#         full_msg += msg.decode('utf-8')
#         if len(full_msg) - 10 == msglen:
#             print("full msg recvd")
#             print(full_msg[10:])
#             new_msg = True
#             full_msg=''
#     print(full_msg)