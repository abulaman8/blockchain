import hashlib
import ecdsa
from ecdsa import VerifyingKey





def double_sha256(data):
    return hashlib.sha256(hashlib.sha256(bytes.fromhex(data)).digest()).hexdigest()


def make_merkle_root(vote_hashes):
        if len(vote_hashes) % 2 != 0:
            vote_hashes.append(vote_hashes[-1])
        temp_vote_hashes = []
        for i in range(0, len(vote_hashes), 2 ):
            concatnated = vote_hashes[i]+vote_hashes[i+1]
            hashed = double_sha256(concatnated)
            temp_vote_hashes.append(hashed)
        vote_hashes = temp_vote_hashes
        if len(vote_hashes) == 1:
            return vote_hashes[0]
        else:
            return make_merkle_root(vote_hashes=vote_hashes)




def deserialize(vbytes):
	msg_type = vbytes[:4].decode('utf-8')
	vote_hash = vbytes[4:36].hex()
	vpub = VerifyingKey.from_string(vbytes[36:100], curve=ecdsa.SECP256k1)
	cpub = VerifyingKey.from_string(vbytes[100:164], curve=ecdsa.SECP256k1)
	time_stamp = int.from_bytes(vbytes[164:168], 'big')
	signature = vbytes[168:]
	data = vbytes[:168]
	return {
		'type': msg_type,
		'vote_hash': vote_hash,
		'vpub': vpub,
		'cpub': cpub,
		'timestamp': time_stamp,
		'signature': signature,
		'data': data
	}









def deserialize_block(block):
    msg_type = block[:4]
    if msg_type != b'blok':
        raise Exception('invalid block')
    size = int(block[4:8].hex(), 16)
    header = block[8:88]
    version = int(header[:4].hex(), 16)
    prev_hash = header[4:36].hex()
    merkle_root = header[36:68].hex()
    time = header[68:72]
    bits = header[72:76]
    nonce = header[76:80]
    if int(block[88].hex(), 16) < 254:
        vote_count = int(block[88].hex(), 16)
        vote_pos = 86
    elif int(block[88].hex(), 16) == 254:
        vote_count = int(block[89:91].hex(), 16)
        vote_pos = 91
    elif int(block[88].hex(), 16) == 255:
        vote_count = int(block[89:93].hex(), 16)
        vote_pos = 93
    else:
        raise Exception('invalid block')
    votes = block[vote_pos:]
    vote_list = []
    for i in range(0, len(votes), 232):
        vote_list.append(deserialize(votes[i:i+232]))
    return {
        'msg_type': msg_type,
        'size': size,
        'header': header.hex(),
        'version': version,
        'prev_hash': prev_hash,
        'merkle_root': merkle_root,
        'time': time,
        'bits': bits,
        'nonce': nonce,
        'vote_count': vote_count,
        'votes': vote_list,
        'current_hash': double_sha256(header)
    }