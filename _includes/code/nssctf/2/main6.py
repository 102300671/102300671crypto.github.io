from Crypto.Util.number import *
from random import choice
from gmpy2 import gcd,invert
'''
flag = b'NSSCTF{******}'
def getMyPrime(nbits):
    while True:
        p = 1
        while p.bit_length() <= nbits:
            p *= choice(sieve_base)
        if isPrime(p+1):
            return p+1
p = getMyPrime(256)
q = getMyPrime(256)
n = p*q
e = 65537
m = bytes_to_long(flag)
c = pow(m, e, n)
print(f'n = {n}')
print(f'e = {e}')
print(f'c = {c}')

'''
n = 53763529836257082401813045869248978487210852880716446938539970599235060144454914000042178896730979463959004404421520555831136502171902051936080825853063287829
e = 65537
c = 50368170865606429432907125510556310647510431461588875539696416879298699197677994843344925466156992948241894107250131926237473102312181031875514294014181272618
a=2
m=2
while True:
    a = pow(a,m,n)
    p = gcd(a-1,n)
    if p!=1 and p!=n:
        break
    m+=1
q=n//p
phi=(p-1)*(q-1)
d=invert(e,phi)
m=pow(c, d, n)
print(long_to_bytes(m))