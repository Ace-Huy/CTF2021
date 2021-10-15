from Crypto.Util.number import getPrime, bytes_to_long

flag = bytes_to_long(open("/challenge/flag.txt", "rb").read())

def genkey():
    e = 0x10001
    p, q = getPrime(256), getPrime(256)
    if p <= q:
      p, q = q, p
    n = p * q
    pubkey = (e, n)
    privkey = (p, q)
    return pubkey, privkey

def encrypt(m, pubkey):
    e, n = pubkey
    c = pow(m, e, n)
    return c

pubkey, privkey = genkey()
c = encrypt(flag, pubkey)

hint = pubkey[1] % (privkey[1] - 1)
print('pubkey:', pubkey)
print('hint:', hint)
print('c:', c)

# e = 65537 

# n = 9205850565099355009233119992333308509057926987587516553442010262770434065524651458723071213422539739783091104957937112504373819793996033829929775503108243 c = 7373290721518384012603108696715714033444163435512092120442505886297149465422635100860419886468382605598579995038885045596223387641682763096919583716818416

# hint = 571338771748514167423682983583747408415015678000205027955504564266299803503