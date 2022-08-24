#code

import cryptography
from cryptography.fernet import Fernet
key = Fernet.generate_key()

with open("secret.key", "wb") as key_file:
    key_file.write(key) 

print(key)


def load_key():
    """""
    load the previously generated key
    """""
    return open("secret.key", "rb").read()


def encrypt_menssage():
    "encrypt menssage"

    key = load_key()
    encoded_menssage = menssage.encode()
    f = Fernet(key)
    encrypt_menssage = f.encrypt(encoded_menssage)

    print(encrypt_menssage)


if __name__ == "__main__":
    encrypt_menssage("texto para criptografar")
