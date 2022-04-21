# from ecdsa import SigningKey, SECP256k1
# import hashlib
# import base58




# sk = SigningKey.generate(curve=SECP256k1)
# s=sk.to_pem()

# vk = sk.verifying_key
# v=vk.to_pem()

# signature = sk.sign(b"message", hashfunc=hashlib.sha256)
# assert vk.verify(signature, b"message", hashfunc=hashlib.sha256)

# sk2 = SigningKey.from_pem(bytearray.fromhex(s.hex()))


# print(s.hex())
# print('--------------------------------------------------------------------------------------------------------')
# print(v.hex())

# print(sk==sk2)





# with open('utxo.pool', 'w') as f:
# 	for i in range(100):
# 		for o in range(2):
# 			f.write(f'{i}:{hashlib.sha256((str(i)+str(o)).encode()).hexdigest()}:#{o}\n')



# with open('utxo.pool', 'r') as f:
# 	lines = f.readlines()
# 	for line in lines:
# 		print(line)


# print(base58.b58encode('AbulAman'.encode()))
# print(base58.b58decode(b'BwK8UCxVTpq').decode())
print(len('5238C71458E464D9FF90299ABCA4A1D7B9CB76AB'))
print(len('b3abaebf7e67a8a98efc109c370e49968e9bb5fe'))