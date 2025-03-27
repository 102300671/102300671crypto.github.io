from Crypto.Util.number import inverse,long_to_bytes
from gmpy2 import isqrt,next_prime
'''
flag = b'NSSCTF{******}'
p = getPrime(512)
q = gmpy2.next_prime(p)
n = p*q
e = 65537
phi = (p-1)*(q-1)
m = bytes_to_long(flag)
c = pow(m, e, n)
print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')
'''
n = 115637000420176820831322601039129424406844427046456738651883381559357542765613732363445112111006849040385859313572091386802534464534403117787314180179562651607533039692795522388596550968316951090748054495960090527479954143448774136390568881020918710834542819900918984139672802889774720153267841255456602500057
e = 65537
c = 98161406745910866780822530171878255235776133393411573803496865047700715941955255328757920065032397556905095591171977170479344602512244671081108703687450560269408412671849929423399172588599903975793985819498354819305128607934552101433664794909855378636055525016664559476808490723554481335856183927702549281730
sn=isqrt(n)
q=next_prime(sn)
p=n//q
phi=(p-1)*(q-1)
d = inverse(e, phi)
m = pow(c, d, n)
print(long_to_bytes(m))