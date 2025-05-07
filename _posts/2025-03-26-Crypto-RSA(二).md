---
layout: default
title: Crypto-RSA(二)
math: true
math_type: svg
---

## nssctf

### [RSA2]P1

{% highlight python linenos %}
{% include code/nssctf/2/main1.py %}
{% endhighlight %}

n很小:

- 低加密指数攻击
- 一般$m^e=c+k \times n$
- 此题$k=0$
- $\text{m}=\sqrt[e]{c}$
  
### [RSA2]P2

{% highlight python linenos %}
{% include code/nssctf/2/main2.py %}
{% endhighlight %}

n很小:

- 低加密指数攻击
- 直接开根不正确
- 遍历`k`，能开出整数根时结束

### [RSA2]P3

{% highlight python linenos %}
{% include code/nssctf/2/main3.py %}
{% endhighlight %}

Rabin:

加密

- 选两个大素数$p$ 和$q$(通常取$p\equiv q\equiv 3 \pmod{4}$)
- 计算$n=p\times q$,公钥:$n(通常为2)$,私钥:$(p,q)$
- 明文$m<n$时,密文$c=m^2 \pmod{n}$

解密

- 计算$p1=c^\frac{p+1}{4} \pmod{p}$
- 计算$q1=c^\frac{q+1}{4}\pmod{q}$
- 通过`CRT`组合四个可能解
  - $m=\pm p1\pmod{p}$
  - $m=\pm q1\pmod{q}$

### [RSA2]P4

{% highlight python linenos %}
{% include code/nssctf/2/main4.py %}
{% endhighlight %}

维纳攻击

- $d$较小时($d<\frac{1}{3}n^\frac{1}{4}$)
- 对$\frac{e}{n}$进行连分数展开，其收敛分数的分母可能是$d$
- 检查$d$，符合条件解

### [RSA3]P5

{% highlight python linenos %}
{% include code/nssctf/2/main5.py %}
{% endhighlight %}

低加密指数广播攻击

- $e=127$,不是很大
- nc连接上后可以获取n和c且有多组
- 中国剩余定理

### [RSA4]P6

{% highlight python linenos %}
{% include code/nssctf/2/main6.py %}
{% endhighlight %}

p-1光滑

- **光滑数**:若一个整数$n$的素因子均 $\leq B$，则称$n$为**B-光滑数**。
- **p-1光滑的意义**:
   当`p`是一个素数且`p-1`是 B-光滑时，意味着`p-1` 可以分解为一系列小素数的乘积。
- `Pollard's p-1`算法  
{% include code/html/a.html %}
