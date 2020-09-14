import binascii
m=bytes("hey", encoding="ascii")
print(binascii.hexlify(m))