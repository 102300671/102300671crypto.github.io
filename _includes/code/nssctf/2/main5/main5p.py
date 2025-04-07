import socket
from sympy.ntheory.modular import crt
import gmpy2 

def collect_data(num=127):
    host = ''node4.anna.nssctf.cn"
    port = 282
    data_list = []
    
    for _ in range(num):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.send(b'1\n')  # 发送选项1触发加密
        response = s.recv(4096).decode()
        n = int(response.split('n: ')[1].split('\n')[0])
        c = int(response.split('c: ')[1].split('\n')[0])
        data_list.append((n, c))
        s.close()
    
    return data_list

def crack_m(data_list):
    n_list = [n for n, _ in data_list]
    c_list = [c for _, c in data_list]
    
    # 使用CRT合并所有同余方程
    M, total_n = crt(n_list, c_list)
    m_e = M % total_n  # 合并后的m^e
    
    # 开e次方恢复明文
    m, is_valid = gmpy2.iroot(m_e, 127)
    if is_valid:
        return bytes.fromhex(hex(m)[2:])
    else:
        raise ValueError("无法开方，可能需要更多数据")

if __name__ == "__main__":
    data = collect_data(127)
    flag = crack_m(data)
    print("Flag:", flag.decode())
