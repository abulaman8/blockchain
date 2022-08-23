import ecdsa
from ecdsa import SigningKey, VerifyingKey
from vote import Vote
from dateutil.tz import gettz
import datetime




class Voter():
	'''
	1. will have a private key
	2. will have a public key

	'''
	def __init__(self):

		
		self.private_key, self.public_key = self.generate_key_pair()
	def generate_key_pair(self):
		private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
		public_key = private_key.verifying_key
		with open('key.pem', 'w') as f:
			f.write(private_key.to_pem().hex())
			f.write('\n---------------------------------------------------------------------------------------\n')
			f.write(public_key.to_pem().hex())
		return private_key.to_pem(), public_key.to_pem()

	def vote(self, candidate_public_key):
		timestamp = datetime.datetime.now(tz=gettz('Asia/Kolkata')).timestamp()
		content = bytes(str({
			"voter": VerifyingKey.from_pem(self.public_key),
			"candidate": candidate_public_key,
			"timestamp": timestamp
		}), 'utf-8')
		signature = SigningKey.from_pem(self.private_key).sign(content)
		vote = Vote(voter_public_key= VerifyingKey.from_pem(self.public_key), timestamp=timestamp , candidate_public_key=candidate_public_key, signature=signature, content=content)
		# print(vote.voter_public_key)
		# print('-------------------------------------------------------------------------------')
		# print('-------------------------------------------------------------------------------')
		# print(vote.candidate_public_key)
		# print('-------------------------------------------------------------------------------')
		# print('-------------------------------------------------------------------------------')
		# print(vote.signature)
		# print('-------------------------------------------------------------------------------')
		# print('-------------------------------------------------------------------------------')
		# print(vote.content)
		# print('-------------------------------------------------------------------------------')
		# print('-------------------------------------------------------------------------------')
		# v = VerifyingKey.from_pem(self.public_key).verify(signature, content)
		# print('-------------------------------------------------------------------------------')
		# print('-------------------------------------------------------------------------------')
		# print(v)






    	


# def mint():
# 	v = Voter()
# 	v.vote(candidate_public_key=1234567890)


# mint()
