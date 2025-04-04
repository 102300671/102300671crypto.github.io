from Crypto.Util.number import long_to_bytes
import gmpy2

def wiener_attack(e, n):
    # 计算 e/n 的连分数展开
    def continued_fraction(e, n):
        cf = []
        while n:
            cf.append(e // n)
            e, n = n, e % n
        return cf

    # 生成收敛分数列表
    def convergents(cf):
        convergents = []
        for i in range(len(cf)):
            numerator, denominator = 1, 0
            for j in range(i, -1, -1):
                numerator, denominator = cf[j] * numerator + denominator, numerator
            convergents.append((numerator, denominator))
        return convergents

    cf = continued_fraction(e, n)
    convergents_list = convergents(cf)

    # 遍历所有收敛分数，寻找可能的 d
    for numerator, denominator in convergents_list:
        if denominator == 0:  # 避免分母为 0
            continue
        if numerator == 0:  # 避免分子为 0
            continue
        if (e * denominator - 1) % numerator != 0:  # 检查是否整除
            continue

        phi = (e * denominator - 1) // numerator

        # 解二次方程 x^2 - (n - phi + 1)x + n = 0 得到 p 和 q
        a = 1
        b = n - phi + 1
        c = n
        discriminant = b * b - 4 * a * c

        if discriminant < 0:  # 判别式小于 0，跳过
            continue

        sqrt_disc = gmpy2.isqrt(discriminant)
        if sqrt_disc * sqrt_disc != discriminant:  # 判别式不是完全平方数，跳过
            continue

        p = (b + sqrt_disc) // 2
        q = (b - sqrt_disc) // 2

        if p * q == n:  # 验证 p 和 q 是否正确
            return denominator, p, q

    return None, None, None

# 输入参数
n = 6969872410035233098344189258766624225446081814953480897731644163180991292913719910322241873463164232700368119465476508174863062276659958418657253738005689
e = 3331016607237504021038095412236348385663413736904453330557803644384818257225138777641344877202234881627514102078530507171735156112302207979925588113589669
c = 1754994938947260364311041300467524420957926989584983693004487724099773647229373820465164193428679197813476633649362998772470084452129370353136199193923837

# 调用 Wiener 攻击函数
d, p, q = wiener_attack(e, n)

if d is not None:
    '''
    print(f'd = {d}')
    print(f'p = {p}')
    print(f'q = {q}')
    '''
    m = pow(c, d, n)
    print(long_to_bytes(m))
else:
    print("Wiener attack failed.")