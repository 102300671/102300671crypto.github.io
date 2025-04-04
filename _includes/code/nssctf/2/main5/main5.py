from Crypto.Util.number import *
import os
flag = os.getenv('FLAG')
m = bytes_to_long(flag.encode())
e = 127
def enc():
    p = getPrime(512)
    q = getPrime(512)
    n = p*q
    c = pow(m, e, n)
    print(f"n: {n}")
    print(f"c: {c}")
def main():
    while True:
        opt = int(input('input> '))
        if opt == 1:
            enc()
main()
