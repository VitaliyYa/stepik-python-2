import simplecrypt

encrypted = open('encrypted.bin', 'rb').read()
passwords = open('passwords.txt').readlines()

for p in passwords:
    p = p.strip()
    try:
        s = simplecrypt.decrypt(p, encrypted)
    except simplecrypt.DecryptionException:
        continue

    print(s.decode('utf-8'))
