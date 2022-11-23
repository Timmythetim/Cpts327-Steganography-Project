from cryptography.fernet import Fernet

key = Fernet.generate_key()
key = key.decode("utf-8")
print(key)

f = open("secretkey.txt", "w")
f.write(key)