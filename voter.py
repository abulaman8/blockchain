import ecdsa
from ecdsa import SigningKey, VerifyingKey
from vote import Vote
from dateutil.tz import gettz
import datetime
import pyqrcode
import png
import hashlib
import socket




HOST = '127.0.0.1'
PORT = 4455
PORT2 = 5555

hps=[('127.0.0.1', 7777), ('127.0.0.1', 9999)]


class Voter():
	'''
	1. will have a private key
	2. will have a public key

	'''
	def __init__(self, private_key=None, public_key=None):

		if private_key and public_key:
			self.private_key = private_key
			self.public_key = public_key
		else:
			self.private_key, self.public_key = self.generate_key_pair()
	def generate_key_pair(self):
		private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
		public_key = private_key.verifying_key
		# hpkey = int.from_bytes(private_key.to_string(), "big")
		# print(hpkey)
		with open('voter_key.pem', 'w') as f:
			f.write(private_key.to_pem().hex())
			f.write('\n---------------------------------------------------------------------------------------\n')
			f.write(public_key.to_pem().hex())
		pbkqr = pyqrcode.create(public_key.to_pem())
		pbkqr.png('voter_public_key.png', scale=6)
		return private_key.to_pem(), public_key.to_pem()

	def vote(self, candidate_public_key, hps=hps):
		vote = Vote(
			voter_public_key=self.public_key,
			voter_private_key=self.private_key,
			candidate_public_key=candidate_public_key
			)
		data = vote.serialize()
		for hp in hps:
			print(hp)
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			connecter = sock
			connecter.connect(hp)
			connecter.send(data)
			connecter.close()
			print(f'data sent to {hp} and closed')

		






    	


def mint():
	vprivate_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
	vpublic_key = vprivate_key.verifying_key.to_pem()
	v = Voter()
	v.vote(candidate_public_key= vpublic_key)

if __name__ == '__main__':
	mint()

# mint()
