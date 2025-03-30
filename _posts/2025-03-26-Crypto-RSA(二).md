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

- 选两个大素数$p$ 和$q$(通常取$p \equiv q \equiv 3 \pmod{4}$)
- 计算$n=p \times q$,公钥:$n$,私钥:$(p,q)$
- 明文$m<n$时,密文$c=m^2 \pmod{n}$
