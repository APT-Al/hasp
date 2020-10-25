import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from RSACipher import RSACipher
import Utils

message = "okan naber"
# print("Original ::",message)

rsa_cipher_enc = RSACipher(Utils.rsa_public_key)
encrypted_text = rsa_cipher_enc.encrypt(message)
# print("Encrypted ::",encrypted_text)

rsa_cipher_dec = RSACipher(Utils.rsa_private_key)
decrypted_text = rsa_cipher_dec.decrypt(encrypted_text)
# print("Plain ::",decrypted_text)

if message == decrypted_text:
    print("TEST IS COMPLETED SUCCESSFULLY")
else:
    print("TEST IS FAILED!")