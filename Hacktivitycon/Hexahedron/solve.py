import gmpy2
from Crypto.Util.number import *

#It is easy to see here that n is very large and e is 
#very small so we can solve this problem by taking the square root of c to get the flag.

c = 2217344750798178599616518881851238192046537371134831984828894413752520937378161486880269974456574131502921272953104454680926482208357166098075344508240480152890914678813031666242202555794691235412837030045499161787224264164243336308650477343133919653356349913604131486721125
m1 = int(gmpy2.iroot(c, 3)[0])
print(long_to_bytes(m1))