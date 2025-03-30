from Crypto.Util.number import inverse, long_to_bytes
from gmpy2 import *
'''
flag = b'NSSCTF{******}'
p = getPrime(256)
q = getPrime(256)
assert p%4 == 3 and q%4 == 3
n = p*q
e = 2
m = bytes_to_long(flag)
c = powmod(m, e, n)
print(f'p = {p}')
print(f'q = {q}')
print(f'e = {e}')
print(f'c = {c}')
'''
p = 67711062621608175960173275013534737889372437946924512522469843485353704013203
q = 91200252033239924238625443698357031288749612243099728355449192607988117291739
e = 2
c = 5251890478898826530186837207902117236305266861227697352434308106457554098811792713226801824100629792962861125855696719512180887415808454466978721678349614
n=p*q
p1=pow(c,(p+1)//4,p)
q1=pow(c,(q+1)//4,q)
p2=-p1
q2=-q1
t1=inverse(p, q)
t2=inverse(q,p)
m1=(p*q1*t1+q*p1*t2)%n
m2=(p*q2*t1+q*p1*t2)%n
m3=(p*q1*t1+q*p2*t2)%n
m4=(p*q2*t1+q*p2*t2)%n
print(long_to_bytes(m1))
print(long_to_bytes(m2))
print(long_to_bytes(m3))
print(long_to_bytes(m4))