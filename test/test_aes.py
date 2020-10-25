import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from AESCipher import AESCipher

key = AESCipher.generate_key(128, True)
# print("KEY ::", key)
cipher = AESCipher(key)

message = "beni sifrelesene yiyorsa"
# print("Plain Text ::",message)

encrypted_text = cipher.encrypt(message)
# print("Encrypted Text ::",encrypted_text)

decrypted_text = cipher.decrypt(encrypted_text)
# print("Decrypted Text ::",decrypted_text)

if message == decrypted_text:
    print("TEST IS COMPLETED SUCCESSFULLY")
else:
    print("TEST IS FAILED!")


