from hashlib import sha256
import socket
from getmac import get_mac_address
from voter import Voter
from pymongo import MongoClient
from vote import deserialize


client = MongoClient('127.0.0.1:27017',
                     username='nodeRunner',
                     password='abulaman',
                     authSource='vsortium',
                     authMechanism='SCRAM-SHA-256')
db = client.vsortium






class Node():
    ''' 
    Inits:
        1. A node will hold a copy of the entire ledger (blockchain) as a list(linked list maybe...) 
        2. will have a MEMPOOL which is a set of all incoming votes
        3. will be listening on a fixed port for votes and blocks
        4. will have a unique id which will be the MAC address of the device it runs on
    Functions:
        1. Verify a vote from the MEMPOOL and add it to a Block
        2. add the "mined" Block to it's copy of the ledger
        3. Broadcast the Block to "known" nodes
        4. Recieve nodes from broadcast (from other nodes) and verify all the votes in it and vote on its status
        5. Request blocks that it has missed from other "known" nodes (Realized when the "prev hash" of an incoming block doesnt match the latest block's hash in it's copy of the ledger)

    '''
    def __init__(self, port=8888):
        self.mempool = []
        self.utxo_pool = db.utxo_pool
        # self.id = str(get_mac_address())
        self.ip = '127.0.0.1'
        self.port = 8888
        self.known_nodes = []
        self.listen()



    def mint(self):
        v = Voter()
        return v

    def verify_vote_and_broadcast(self, vote):
        vote_dict = deserialize(vote)
        valid_voter = self.utxo_pool.find_one({'pub_key': int.from_bytes(vote_dict.vpub, "big")})
        if valid_voter:
            self.mempool.append(vote)
            for node in self.known_nodes:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(node)
                sock.send(vote)
                sock.close()
                print(f'vote broadcasted to {node[0]}')
    

    def mine(self):
        pass


    def listen(self):
        listener_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener_sock.bind((self.ip, self.port))
        listener_sock.listen(10)
        while True:
            client_socket, address = listener_sock.accept()
            print(f'connection from {address}...')
            msg = client_socket.recv(1024)
            if msg[:4].decode('utf-8') == 'vote':
                self.verify_vote_and_broadcast(msg)
            print(msg)
    

    def request_missed_blocks(self):
        pass    

    def broadcast_block(self, block):
        pass



n = Node()
n.mint()






