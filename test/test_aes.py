import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
from AESCipher import AESCipher
import base64
import hashlib

password = AESCipher.generate_key(16)
iv = AESCipher.generate_key(16)
# print("KEY ::", key)
cipher = AESCipher(password)

# message = b"beni sifrelesene yiyorsa"
# print("Plain Text ::",message)
# encrypted_text = cipher.encrypt(iv, message)
# print("IV::", iv, ":: Encrypted Text ::",encrypted_text)
# decrypted_text = cipher.decrypt(iv, encrypted_text)
# print("Decrypted Text ::",decrypted_text)

# if message == decrypted_text:
#     print("STRING ENCRYPTION TEST IS COMPLETED SUCCESSFULLY")
# else:
#     print("STRING ENCRYPTION TEST IS FAILED!")


inf = "test_image.jpeg"
midf = "cogii.enc"
outf = "cikti_"+inf
chunk_size = 16*1024 # 16 byte

with open(inf, 'rb') as infile:
    with open(midf, 'wb') as outfile:
        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            outfile.write(cipher.encrypt(iv, chunk))

with open(midf, 'rb') as infile:
    with open(outf, 'wb') as outfile:
        while True:
            chunk = infile.read(chunk_size)
            if len(chunk) == 0:
                break
            outfile.write(cipher.decrypt(iv, chunk))