---
layout: default
title: Crypto-RSA(一)
math: true
math_type: svg
---

# nssctf

## [RSA1]P1

{% raw %}{% highlight python linenos %}
{% include_code "nssctf/一/main1.py" lang=python %}
{% endhighlight %}{% endraw %}

常规RSA解法:

- 由`p`,`q`求`n`和欧拉函数`phi`
- 由`e`,`phi`求逆元`d`
- 由`c`,`d`,`n`求`m`
- 整数`m`转为字节流

## [RSA1]P2

{% include_code "nssctf/一/main2.py" lang=python %}

n可分解:

- 用[factordb](https://factordb.com/)或`yafu`分解`n`得到`p`,`q`
- 常规RSA解法

[RSA1]P3

{% include_code "nssctf/一/main3.py" lang=python %}

n可分解

[RSA1]P4

{% include_code "nssctf/一/main4.py" lang=python %}

`p`,`q`接近
- $n = p \times q$
- $\text{sn} = \sqrt{n}$
- $q = \mathrm{next\\_prime}(p)$
- $p = \left\lfloor \frac{n}{q} \right\rfloor$
- 常规RSA解法
