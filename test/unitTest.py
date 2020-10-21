import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from AESCipher import AESCipher

key = AESCipher.generate_key(128, True)
print("KEY ::", key)
cipher = AESCipher(key)

plain_text = "beni sifrelesene yiyorsa"
print("Plain Text ::",plain_text)

cipher_text = cipher.encrypt(plain_text)
print("Encrypted Text ::",cipher_text)

decrypted_text = cipher.decrypt(cipher_text)
print("Decrypted Text ::",decrypted_text)


