



class Vote():
	'''
	1. will have the voter's public key
	2. will have the transaction specific data
	3. will have reciever's public key
	4. will have a digital signature (using the voter's private key)
	'''
	def __init__(self, voter_public_key, candidate_public_key, signature, content, timestamp):
		self.voter_public_key = voter_public_key
		self.candidate_public_key = candidate_public_key
		self.timestamp = timestamp
		self.content = content
		self.signature = signature
		print(self.signature)