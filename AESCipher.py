import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES

"""
TODO write a description for this class

https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
https://stackoverflow.com/questions/12524994/encrypt-decrypt-using-pycrypto-aes-256
"""

class AESCipher(object):
    def __init__(self,key):
        """
            test_function does blah blah blah.

            :key: describe about parameter key
            :return: describe what it returns

            SHA256 gives out a 32-byte hash that is a perfect-sized key for AES256. 
            Generation/derivation of a key is assumed to be random/secure and should be out of the encryption/decryption code's scope. 
            Hashing is just a guarantee that the key is usable with the selected cipher
        """
        self.block_size = 32
        self.key = hashlib.sha256(key).digest()

    def encrypt(self, iv, raw):
        raw = self._pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.encrypt(raw)

    def decrypt(self, iv, enc):
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return cipher.decrypt(enc)

    def _pad(self, chunk):
        # if len(chunk) == 0:
        #     return chunk
        # elif len(chunk) % self.block_size != 0:
        return chunk + b' ' * (self.block_size - len(chunk) % self.block_size)

    def generate_iv():
        return Random.new().read(AES.block_size)

    def generate_key(bits, encode=False):
        generated = Random.OSRNG.posix.DevURandomRNG()
        content = generated.read(bits)
        
        if(encode):
            return base64.b64encode(content)

        return content