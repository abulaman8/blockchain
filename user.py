import ecdsa
from hashlib import sha256, new
from transaction import Transaction



class User():
	'''
	1. will have a private key
	2. will have a public key
	3. will have an address
	4. will have a balance
	5. will have a list of all transactions

	'''
	def __init__(self):

		
		self.private_key, self.public_key = self.generate_key_pair() 
		self.address = new('ripemd160', sha256(self.public_key).hexdigest().encode()).hexdigest()
		self.can_vote = False
		self.can_recieve_vote = False
		self.voted = False
		# print(self.public_key)
		# print(self.private_key)
		print(self.address)
	def generate_key_pair(self):
		private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
		public_key = private_key.verifying_key
		# print(private_key.to_string())
		# print(len(public_key.to_string()))
		with open('key.pem', 'w') as f:
			f.write(private_key.to_pem().hex())
			f.write('\n---------------------------------------------------------------------------------------\n')
			f.write(public_key.to_pem().hex())
		return private_key.to_pem(), public_key.to_pem()

	def vote(self, reciever_address, value):
		Transaction(self.address, self.public_key, reciever_address, value, 1)





	def mint(self):
		pass



u = User()