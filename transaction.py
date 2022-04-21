class Transaction():
	'''
	1. will have the sender's public key
	2. will have the transaction specific data
	3. will have reciever's public key
	4. will have a digital signature (using the sender's private key)
	'''
	def __init__(self, sender_address, sender_public_key, reciever_address, value, inputUTXO):
		self.sender_address = sender_address
		self.sender_public_key = sender_public_key
		self.reciever_address = reciever_address
		self.value = value
		self.script = f"op_dup op_hash160 {reciever_address} op_equalverify op_checksig"
		self.input = inputUTXO
		self.output = 'output'
		self.signature = {
		"input": self.input,
		"output": self.output


		}
		print(self.signature)