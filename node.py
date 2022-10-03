import socket
from pymongo import MongoClient
import sys
import os


from utils import make_merkle_root, deserialize, deserialize_block
from voter import Voter
from block import Block



client = MongoClient('127.0.0.1:27017',
                     username='nodeRunner',
                     password='abulaman',
                     authSource='vsortium',
                     authMechanism='SCRAM-SHA-256')
db = client.vsortium

args = sys.argv

port = int(args[1])

known_nodes=[]

dns_file = args[2]
with open(dns_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        known_nodes.append((line.split(',')[0], int(line.split(',')[1])))


class Node():
    ''' 
    Inits:
        1. A node will hold a copy of the entire ledger (blockchain) as a list(linked list maybe...) 
        2. will have a MEMPOOL which is a set of all incoming votes
        3. will be listening on a fixed port for votes and blocks
    Functions:
        1. Verify a vote from the MEMPOOL and add it to a Block
        2. add the "mined" Block to it's copy of the ledger
        3. Broadcast the Block to "known" nodes
        4. Recieve nodes from broadcast (from other nodes) and verify all the votes in it and vote on its status
        5. Request blocks that it has missed from other "known" nodes (Realized when the "prev hash" of an incoming block doesnt match the latest block's hash in it's copy of the ledger)

    '''
    def __init__(
        self,
        prev_hash,
        port=8888,
        known_nodes = [],
        target='00000000000015dbd20000000000000000000000000000000000000000000000',
        blocks_path = os.path.join(os.path.join(os.getcwd(), 'blocks')),
        block_height = 0
    ):
        self.mempool = []
        self.utxo_pool = db.utxo_pool
        self.ip = '127.0.0.1'
        self.port = port
        self.known_nodes = known_nodes
        self.target = target
        self.prev_hash = prev_hash
        self.version_number = 0
        self.blocks_path = blocks_path
        self.block_height = block_height
        self.listen()
        



    def mine_block(self):
        if len(self.mempool) > int('ffffffff', 16):
            votes = self.mempool[:int('ffffffff', 16)]
        else:
            votes = self.mempool
        new_block = Block(prev_hash=self.prev_hash, version_number=self.version_number, target=self.target, votes=votes)
        block = new_block.mine()
        self.broadcast_block(block=block)

    def mint(self):
        v = Voter()
        return v

    def verify_vote_and_broadcast(self, vote):
        print('started')
        vote_dict = deserialize(vote)
        valid_voter = self.utxo_pool.find_one({'pub_key': str(int.from_bytes(vote_dict['vpub'].to_string(), "big"))})
        if valid_voter and vote_dict['vpub'].verify(vote_dict['signature'], vote_dict['data']):
            self.mempool.append(vote)
            for node in self.known_nodes:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.connect(node)
                sock.send(vote)
                sock.close()
                print(f'vote broadcasted to {node[0]}')
        else:
            print('voter not in database')
    



    def listen(self):
        listener_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener_sock.bind((self.ip, self.port))
        listener_sock.listen(10)
        print(f'listening on {self.ip}:{self.port}')
        while True:
            client_socket, address = listener_sock.accept()
            print(f'connection from {address}...')
            msg = client_socket.recv(1024)
            if msg[:4].decode("utf-8") == 'vote':
                print('its a vote')
                self.verify_vote_and_broadcast(msg)
                print('sent for broadcast')
            elif msg[:4].decode("utf-8") == 'blok':
                print('it\'s a block')
                self.verify_block_and_broadcast(msg)
                print('sent block for verification and broadcast')
            else:
                print('its neither a vote nor a block')
            print(msg)
    

    def request_missed_blocks(self):
        pass

    def verify_block_and_broadcast(self, block):
        block_data = deserialize_block(block=block)
        if block_data['prev_hash'] == self.prev_hash:
            vote_hashes = [vote['vote_hash'] for vote in block_data['votes']]
            if block_data['merkle_root'] == make_merkle_root(vote_hashes=vote_hashes):
                for vote in block_data['votes']:
                    vpub = self.utxo_pool.find_one({'pub_key': str(int.from_bytes(vote['vpub'].to_string()))})
                    if vpub:
                        pass
                    else:
                        raise Exception('Voter not in database, or has already voted')
            else:
                raise Exception('Invalid Merkle root or the block has been altered')
        else:
            raise Exception('Invalid previous block hash')
        self.prev_hash = block_data['prev_hash']
        with open(f'vblk{self.block_height+1}.dat', 'wb') as bfile:
            bfile.write(block)
        
        for node in self.known_nodes:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(node)
            sock.send(block)
            sock.close()
            print(f'vote broadcasted to {node[0]}')

    def broadcast_block(self, block):
        for node in self.known_nodes:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(node)
            sock.send(block)
            sock.close()
            print(f'vote broadcasted to {node[0]}')



n = Node(port=port, known_nodes=known_nodes)
# n.mint()






