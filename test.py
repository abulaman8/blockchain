# import hashlib
import ecdsa
# from ecdsa import VerifyingKey, SigningKey, SECP256k1
from vote import Vote
from block import Block
from utils import deserialize_block
# from pymongo import MongoClient






# client = MongoClient('127.0.0.1:27017',
#                      username='nodeRunner',
#                      password='abulaman',
#                      authSource='vsortium',
#                      authMechanism='SCRAM-SHA-256')
# db = client.vsortium
# utxo_pool = db.utxo_pool








# for i in range(1500):
#     with open(f'test_voters/{i}.voter', 'wb') as f:
#         prvk = SigningKey.generate(curve=SECP256k1)
#         pubk = prvk.verifying_key
#         utxo_pool.insert_one({
#             'pub_key': str(int.from_bytes(pubk.to_string(), "big"))
#         })
#         f.write(prvk.to_string())
#         f.write(b'0000000000000000000000000000000000000000000000000000000000000000000000000000')
#         f.write(pubk.to_string())
#     print(i)


# from voter import Voter

# hps=[('127.0.0.1', 7777), ('127.0.0.1', 9999)]

# cprv = SigningKey.generate(curve=SECP256k1)
# cpub = cprv.verifying_key.to_pem()

# v = Voter()
# utxo_pool.insert_one({
#     'pub_key': str(int.from_bytes(VerifyingKey.from_pem(v.public_key).to_string(), "big"))
# })

# v.vote(candidate_public_key=cpub)


# prv = SigningKey.generate(curve = SECP256k1)
# pub = prv.verifying_key
# msg = b'abulaman'
# sig = prv.sign(data=msg)
# print(pub.verify(sig, msg))


# a = '00000000000000000696f4000000000000000000000000000000000000000000'
# # print(len(a))
# # for i in range(0, len(a), 2):
# #     if a[i] + a[i+1] == '00':
# #         a = a[i+2:]
# #         print(a)
# #     else:
# #         break
# # print(a)
# b = int(a, 16)
# c=f'{b:x}'



# a=b'abcdefghijklmnopqrstuvwxyz'
# l = []
# for i in range(0, len(a), 2):
#     l.append(a[i:i+2])
# print(l)



# class Pair():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self,):
#         return self


def vote():
    vprivate_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    vpublic_key = vprivate_key.verifying_key.to_pem()
    cprivate_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
    cpublic_key = cprivate_key.verifying_key.to_pem()
    vote = Vote(candidate_public_key=cpublic_key, voter_private_key=vprivate_key.to_pem(), voter_public_key=vpublic_key)
    vs = vote.serialize()
    print('\n')
    print('VOTE:')
    print('\n')
    print(vs)
    print('\n')
    print(f'len of vote: {len(vs)}')
    return vs

prev_hash = '0000000000000000000000000000000000000000000000000000000000000000'
target = 'ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff'
vote = vote()
votes = []
votes.append(vote)
print(f'votes_list: {votes}')
# votes = [b'voteh$\xd5\xf7\x15%\x03\n\x1f#\xe5\x8bmS\x0b`1\xfao\r\xd1\xd9y\x8f\xa8M\xf1c\xde#x\xc9k\xc2\xfc\xd7\xb8\xa5\x1e\t+\xb9:\x9f\xe2\xd9\xcd\x05\xf5\x96\x18m\x8b\x1f\x9f\xea\xe0\x86go\x82\x95(\xde6k\x12r2$)>\xc6\x82\x91\xf3\x0f6\xce\x95\x06\xb3GI\xaf\xc5\xb4X/\xf6\xe0\xe6Q\xd6\xeb\xae\x85\xee\x85\x820\xbdng\xc9\xc3\xe5\x08\xd1\x84\xda\xd4\xf5\xe5\xf6\x824\xa5\x18\xf3\x1d\x14~\x1e\x07J\xf1\xf6\x0b\xae{\xc41\xb2\xe9\xca\x94\x04\xa3\x8a\x070`\xe9\xfd\xd4\xce\x86!\x9fM\x01\x076\xd8-\xc0\n>\x02c:\x9e*`\x9cGm\xd5a\xf0"+&12W\xbd\xb5}\xab\xcfW\x1c\xebf\xf5Y\xc6f9\xb6hO\x172u>\x8e6s0\x0fM\x89a"\x93d\xfe\xe6\xd9\x95\xbcnfd\xad\xff\xd9/h}f\xd9\x94\xeb\xc7']
version = 0

block = Block(prev_hash=prev_hash, target=target, votes=votes, version_number=version)

mined_block = block.mine()

print('BLOCK:\n')
print(mined_block)

block_data = deserialize_block(mined_block)

print('BLOCK DATA:\n')
print(block_data)






