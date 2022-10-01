import datetime
import hashlib
from dateutil.tz import gettz
from utils import double_sha256, make_merkle_root, deserialize


class Block():
    def __init__(self, prev_hash, version_number, votes, target):
        self.prev_hash = prev_hash
        self.version_number = version_number
        self.votes = votes
        self.time = int(datetime.datetime.now(tz=gettz('Asia/Kolkata')).timestamp())
        self.target = target
        self.bits = self.target_to_bits()
        self.vote_hashes = []
        self.vote_count = len(votes)
        for vote in self.votes:
            deserialised_vote = deserialize(vote)
            vote_hash = deserialised_vote['vote_hash']
            self.vote_hashes.append(vote_hash)
        self.merkle_root = make_merkle_root(vote_hashes=self.vote_hashes)
    
    def target_to_bits(self):
        str_target = str(int(self.target, 16))
        if len(str_target) % 2 != 0:
            str_target = '0'+str_target
        bits = f'{len(str_target):x}{str_target[:6]}'
        return bits
    

    def mine(self):
        msg_type = b'blok'
        block_header = self.construct_header()
        i=0
        if len(bytes.fromhex(hex(self.vote_count))) == 1:
            vote_count = hex(self.vote_count)
        elif len(bytes.fromhex(hex(self.vote_count))) == 2:
            i=254
            h = i.to_bytes(1, "big").hex()
            vote_count = h + hex(self.vote_count)
        elif len(bytes.fromhex(hex(self.vote_count))) == 3 or len(bytes.fromhex(hex(self.vote_count))) == 4:
            i=255
            h = i.to_bytes(1, "big").hex()
            vote_count = h + hex(self.vote_count)
        else:
            raise Exception('Too many votes in block.')
        vote_data = b''.join(self.votes)
        size = (len(bytes.fromhex(block_header)) + len(bytes.fromhex(vote_count)) + len(vote_data)).to_bytes(4, "big").hex()
        return msg_type + bytes.fromhex(size + block_header + vote_count) + vote_data

        

    def construct_header(self):
        
        version_bytes = self.version_number.to_bytes(4, "big")
        merkle_bytes = bytes.fromhex(self.merkle_root)
        time_bytes = self.time.to_bytes(4, "big")
        bits = bytes.fromhex(self.bits)
        nonce = 0
        header_content = version_bytes+self.prev_hash+merkle_bytes+time_bytes+bits
        while True:
            header_hash = double_sha256(header_content+nonce.to_bytes(4, "big"))
            if int(header_hash, 16) < int(self.target, 16):
                break
            else:
                nonce+=1
        nonce_bytes = nonce.to_bytes(4, "big")
        return header_content.hex()+nonce_bytes.hex()








    
    


        