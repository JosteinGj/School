import binascii

def toHex(word):
    return int(str(binascii.hexlify(word), 'ascii'), 16)

def toString(word):
    return str(binascii.unhexlify(hex(word)[2:]), 'ascii')

def encrypt(m,key):
    m = bytes(m, encoding='ascii')

    key = bytes(key, encoding='ascii')
    hex_m=toHex(m)
    hex_key=toHex(key)
    code=hex_m^hex_key
    return toString(code)

def decrypt(code,key):
    code =bytes(code, encoding="ascii")
    key = bytes(key, encoding='ascii')
    hex_c= toHex(code)
    hex_key = toHex(key)
    message = hex_c ^ hex_key
    return toString(message)


