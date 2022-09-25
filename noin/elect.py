from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

# Generate our key
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

# Write our key to disk for safe keeping
with open('keys/key.pem', 'wb') as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(
            b'some_kind_of_password'),
    ))

with open('keys/key.pem', 'rb') as f:
    pem_data = f.read()
    rkey = load_pem_private_key(
        pem_data,
        password=b'some_kind_of_password'
    )
    print(rkey.decrypt())


# print(load_pem_public_key(key))
