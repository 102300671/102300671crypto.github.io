from pwn import *
import re
from functools import reduce
import gmpy2
from math import gcd
from tqdm import tqdm

def collect_data(host, port, count=127):
    n_list = []
    c_list = []
    with tqdm(total=count, desc="数据收集进度") as pbar:
        for _ in range(count):
            try:
                r = remote(host, port)
                r.sendlineafter(b'input> ', b'1')
                data = r.recvall().decode()
                r.close()

                n_match = re.search(r'n:\s*(\d+)', data)
                c_match = re.search(r'c:\s*(\d+)', data)
                if n_match and c_match:
                    n = int(n_match.group(1))
                    c = int(c_match.group(1))
                    n_list.append(n)
                    c_list.append(c)
                    print(f"已收集 {len(n_list)} 组数据")
                else:
                    print("数据解析失败，跳过当前连接")
                pbar.update(1)
            except ConnectionError:
                print("连接异常，重试...")
            except ValueError:
                print("数据转换错误，跳过当前连接")
    return n_list, c_list

def crt(c_list, n_list):
    # 中国剩余定理计算 C ≡ c_i mod n_i
    N = reduce(lambda a, b: a * b, n_list)
    result = 0
    for c, n in zip(c_list, n_list):
        Ni = N // n
        inv = gmpy2.invert(Ni, n)
        result += c * Ni * inv
    return result % N

def are_coprime(n_list):
    for i in range(len(n_list)):
        for j in range(i + 1, len(n_list)):
            if gcd(n_list[i], n_list[j]) != 1:
                return False
    return True

def main():
    host = "node4.anna.nssctf.cn"
    port = 28561

    n_list, c_list = collect_data(host, port, 127)
    if len(n_list) < 127:
        print("数据不足 127 组，攻击失败")
        return
    if not are_coprime(n_list):
        print("n 之间存在非互质情况，攻击失败")
        return

    # 计算 CRT 组合值 C = m^127
    C = crt(c_list, n_list)

    # 开 127 次方恢复 m
    m, is_valid = gmpy2.iroot(C, 127)
    if is_valid:
        flag = bytes.fromhex(hex(m)[2:]).decode('utf-8', errors='ignore')
        print(f"成功恢复明文: {flag}")
    else:
        print("攻击失败：无法对 C 开 127 次方")

if __name__ == "__main__":
    main()