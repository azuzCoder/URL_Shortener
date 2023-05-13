from django.contrib.auth.hashers import PBKDF2PasswordHasher

h = PBKDF2PasswordHasher()
enc = h.encode('salom', '1')
print(enc.split('$')[-1])


