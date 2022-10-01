# import hashlib
# from ecdsa import VerifyingKey, SigningKey, SECP256k1
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