from __future__ import unicode_literals
import base64
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 
class RSACipher(object):

    def __init__(self, key):
        _key_object = RSA.importKey(key)
        self.cipher = PKCS1_v1_5.new(_key_object)

    def encrypt(self, plain_text):
        return self.cipher.encrypt(plain_text)

    def decrypt(self, cipher_text):
        return self.cipher.decrypt(cipher_text,None)