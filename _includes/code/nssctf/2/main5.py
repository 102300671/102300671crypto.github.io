from gmpy2 import iroot,invert
from pwn import *
from Crypto.Util.number import long_to_bytes
'''
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
'''
def crt(n_list, c_list):
    n = 1
    for i in n_list:
        n *= i
    N = []
    for i in n_list:
        N.append(n//i)
    t = []
    for i in range(len(n_list)):
        t.append(invert(N[i], n_list[i]))

    summary = 0
    for i in range(len(n_list)):
        summary = (summary + c_list[i]*t[i]*N[i]) % n
    return summary


io = remote('node4.anna.nssctf.cn', 28533)
e = 127
n_list = []
c_list = []
for i in range(127):
    io.sendlineafter(b'input> ', b'1')  # 等待收到input> 后发送1
    n = int(io.recvline().decode()[2:])  # 接收一行数据 即 n: xxxx
    c = int(io.recvline().decode()[2:])  # 接收一行数据 即 c: xxxx
    n_list.append(n)
    c_list.append(c)
    
M = crt(n_list,c_list)
m = iroot(M,e)[0]
flag = long_to_bytes(m)
print(flag)

