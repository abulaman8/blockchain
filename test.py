from ecdsa import VerifyingKey, SigningKey, SECP256k1

for i in range(1500):
    with open(f'test_voters/{i}.voter', 'wb') as f:
        prvk = SigningKey.generate(curve=SECP256k1)
        pubk = prvk.verifying_key
        f.write(prvk.to_string())
        f.write(b'0000000000000000000000000000000000000000000000000000000000000000000000000000')
        f.write(pubk.to_string())
    print(i)