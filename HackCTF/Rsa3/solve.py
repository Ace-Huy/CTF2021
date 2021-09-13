from gmpy2 import *
from Crypto.Util.number import *

c = 0x5c93ba85692a8b3981a5d47be0e80d129b8a2f6cf4dc134547aa7e1620f6691513b1dc1d69e085c39e261c2b49026436bb243dba70a86f7fcd1a3a7e6b0f0ecfac015becad0a76e9cf208d5d31e2b4865
 
with local_context() as ctx:
 
    ctx.precision = 3000
 
    m = cbrt(c)
   
    print (long_to_bytes(m))