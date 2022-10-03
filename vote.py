
import ecdsa
from ecdsa import VerifyingKey, SigningKey
from dateutil.tz import gettz
import datetime
import hashlib

class Vote():
	'''
	1. will have the voter's public key
	2. will have the transaction specific data
	3. will have reciever's public key
	4. will have a digital signature (using the voter's private key)
	'''
	def __init__(self, voter_public_key, candidate_public_key, voter_private_key):
		self.vpub = VerifyingKey.from_pem(voter_public_key)
		self.cpub = VerifyingKey.from_pem(candidate_public_key)
		self.timestamp = int(datetime.datetime.now(tz=gettz('Asia/Kolkata')).timestamp())
		self.vprv = SigningKey.from_pem(voter_private_key)
		
	def serialize(self):
		msg_type = b'vote'                                                                              #4 bytes
		# print(f'')
		vpub_bytes = self.vpub.to_string()                                                              #64 bytes
		cpub_bytes = self.cpub.to_string()                                                              #64 bytes
		time_bytes = self.timestamp.to_bytes(4, "big")                                                  #4 bytes
		content = vpub_bytes + cpub_bytes + time_bytes                                                  #136 bytes 
		# print(content)
		# print(type(content))
		content_hash = hashlib.sha256(content).hexdigest()                                              #32 bytes
		txn_bytes = msg_type + bytes.fromhex(content_hash)+content                                      #168 bytes
		signature = self.vprv.sign(txn_bytes)                                                           #64 bytes
		# print(len(signature))

		return txn_bytes + signature                                                                    #232 bytes




