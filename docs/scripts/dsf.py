from Crypto.Util.number import bytes_to_long, long_to_bytes
from Crypto.Random import get_random_bytes 
import Crypto
import libnum

bits = 128
msg = "en NSI on fait de la crypto"

p = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)
q = Crypto.Util.number.getPrime(bits, randfunc=get_random_bytes)

n = p*q
phi = (p-1)*(q-1)

e = 65537
d = libnum.invmod(e,phi)

m = bytes_to_long(msg.encode('utf-8'))

c = pow(m,e, n)
res = pow(c,d ,n)

print(long_to_bytes(res))
