import encryption

encr = encryption.Encryption()

a = encr.enc("hello")

print(a)

print(encr.dec(a))
