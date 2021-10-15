from Crypto.PublicKey import RSA 
from Crypto.Util.number import *
f = open("privatekey.pem", "r")
key = RSA.importKey(f.read())
n = key.n
p = key.p
q = key.q

phi = (p-1)*(q-1)
c = 1703380908157528283172041137132390349496157838445725605013427432689517712852707895688494322667218403379009536599334770578485119117275052717689607980637948
d = pow(65537,-1,phi)
m = pow(c,d,n)
print(long_to_bytes(m))

#b'}drah_taht_t0n_s1_ASR{OD'
#b'DO{RSA_1s_n0t_that_hard}'