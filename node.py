from hashlib import sha256
import socket
from getmac import get_mac_address
 

class Node():
    ''' 
    Inits:
        1. A node will hold a copy of the entire ledger (blockchain) as a list(linked list maybe...) 
        2. will have a MEMPOOL which is a set of all incoming transactions
        3. will be listening on a fixed port for transactions and blocks
        4. will have a unique id which will be the MAC address of the device it runs on
    Functions:
        1. Verify a transaction from the MEMPOOL and add it to a Block
        2. add the "mined" Block to it's copy of the ledger
        3. Broadcast the Block to "known" nodes
        4. Recieve nodes from broadcast (from other nodes) and verify all the transactions in it and vote on its status
        5. Request blocks that it has missed from other "known" nodes (Realized when the "prev hash" of an incoming block doesnt match the latest block's hash in it's copy of the ledger)

    '''
    def __init__(self, port=8888):
        self.block_chain = []
        self.mempool = []
        self.id = str(get_mac_address())
        self.ip = socket.gethostbyname(socket.gethostname())
        self.port = port
        self.known_nodes = []
        # self.sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.reciever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sender.bind(('127.0.0.1', self.port))
        # self.sender.listen()

        print(self.port)
        print(self.id)
        print(self.ip)
    def verify_transaction_and_broadcast(self, transaction):

        pass
    

    def mine(self):
        pass


    def listen(self):
        pass
    

    def request_missed_blocks(self):
        pass    

    def broadcast_block(self, block):
        pass



n = Node()







