from Crypto.Util.number import long_to_bytes,inverse
from gmpy2 import isqrt
'''
flag = b'NSSCTF{******}'

p = getPrime(512)
q = getPrime(512)

e = 65537*2

n = p*q

m = bytes_to_long(flag)

c = pow(m, e, n)

print(f'p = {p}')
print(f'q = {q}')
print(f'e = {e}')
print(f'c = {c}')

'''
p = 9927950299160071928293508814174740578824022211226572614475267385787727188317224760986347883270504573953862618573051241506246884352854313099453586586022059
q = 9606476151905841036013578452822151891782938033700390347379468858357928877640534612459734825681004415976431665670102068256547092636766287603818164456689343
e = 131074
c = 68145285629092005589126591120307889109483909395989426479108244531402455690717006058397784318664114589567149811644664654952286387794458474073250495807456996723468838094551501146672038892183058042546944692051403972876692350946611736455784779361761930869993818138259781995078436790236277196516800834433299672560
e=e//2
phi=(p-1)*(q-1)
d=inverse(e,phi)
n=p*q
m=pow(c,d,n)
m=isqrt(m)
print(long_to_bytes(m))