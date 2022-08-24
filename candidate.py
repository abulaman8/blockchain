import ecdsa
from ecdsa import SigningKey, VerifyingKey
import pyqrcode
import png


class Candidate():
    def __init__(self):
        self.private_key, self.public_key = self.generate_key_pair()
    
    def generate_key_pair(self):
        private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        public_key = private_key.verifying_key
        with open('candidate_key.pem', 'w') as f:
            f.write(private_key.to_pem().hex())
            f.write('\n---------------------------------------------------------------------------------------\n')
            f.write(public_key.to_pem().hex())
        pbkqr = pyqrcode.create(public_key.to_pem())
        pbkqr.png('candidate_public_key.png', scale=6)
        return private_key.to_pem(), public_key.to_pem()