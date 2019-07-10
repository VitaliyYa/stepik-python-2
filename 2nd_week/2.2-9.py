# lib simple-crypt
import urllib.request
from simplecrypt import encrypt, decrypt, DecryptionException
#
# password = '123'
# ciphertext = encrypt(password, 'my secret message')
# print(ciphertext)
# plaintext = decrypt(password, ciphertext)
# print(plaintext)

url_file_encrypted = 'https://stepic.org/media/attachments/lesson/24466/encrypted.bin'
url_file_passwords = 'https://stepic.org/media/attachments/lesson/24466/passwords.txt'
file_encrypted = 'encrypted.bin'
file_passwords = 'passwords.txt'

encrypted_open = urllib.request.urlopen(url_file_encrypted).read()
passwords_open = urllib.request.urlopen(url_file_passwords).read().strip().split()

with open(file_encrypted, 'rb') as line:
    encrypted = line.read()

with open(file_passwords, 'rb') as p:
    passwords = p.read().strip().split()

for p in passwords:
    try:
        plain = decrypt(p, encrypted)
    except DecryptionException:
        pass
    else:
        plain = decrypt(p, encrypted)
        print(plain)

# print(encrypted)
print(passwords)
