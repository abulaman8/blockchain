from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from hashlib import sha256
from .transaction import Transaction


class User():
	'''
	1. will have a private key
	2. will have a public key
	3. will have an address
	4. will have a balance
	5. will have a list of all transactions

	'''
	def __init__(self):

		self.public_key, self.private_key, self.key_pair = self.generate_key_pair()
		self.address = sha256(self.public_key).hexdigest()
	def generate_key_pair(self):
		key_pair = DSA.generate(2048)
		with open('keyfile.pem', 'wb') as f:
			f.writelines([key_pair.export_key(), key_pair.publickey().export_key()])
		return key_pair.publickey().export_key(), key_pair.export_key(), key_pair
	def create_transaction(self, reciever_address, value):
		hash = SHA256.new(value)

		signature = DSS.new(self.key_pair, 'flips-186-3').sign(hash)
		return Transaction(sender_address=self.address, 
		sender_public_key=self.public_key, 
		reciever_address=reciever_address,
		value = value,
		signature=signature
		)


u = User()