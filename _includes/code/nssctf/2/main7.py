from Crypto.Util.number import *
from random import choice
from sympy import sieve
from math import gcd
'''
flag = b'NSSCTF{******}'
def getMyPrime(nbits):
    while True:
        p = 1
        while p.bit_length() <= nbits:
            p *= choice(sieve_base)
        if isPrime(p-1):
            return p-1
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
n = 63398538193562720708999492397588489035970399414238113344990243900620729661046648078623873637152448697806039260616826648343172207246183989202073562200879290937
e = 65537
c = 26971181342240802276810747395669930355754928952080329914687241779532014305320191048439959934699795162709365987652696472998140484810728817991804469778237933925
