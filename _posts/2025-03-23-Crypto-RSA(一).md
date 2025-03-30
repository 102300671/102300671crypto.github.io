---
layout: default
title: Crypto-RSA(一)
math: true
math_type: svg
---

## nssctf

### [RSA1]P1

{% highlight python linenos %}
{% include code/nssctf/1/main1.py %}
{% endhighlight %}

常规RSA解法:

- 由`p`,`q`求`n`和欧拉函数`phi`
- 由`e`,`phi`求逆元`d`
- 由`c`,`d`,`n`求`m`
- 整数`m`转为字节流

### [RSA1]P2

{% highlight python linenos %}
{% include code/nssctf/1/main2.py %}
{% endhighlight %}

n可分解:

- 用[factordb](https://factordb.com/)或`yafu`分解`n`得到`p`,`q`
- 常规RSA解法

### [RSA1]P3

{% highlight python linenos %}
{% include code/nssctf/1/main3.py %}
{% endhighlight %}

n可分解

### [RSA1]P4

{% highlight python linenos %}
{% include code/nssctf/1/main4.py %}
{% endhighlight %}

`p`,`q`接近

- $n = p \times q$
- $\text{sn} = \sqrt[e]{n}$
- $q = \mathrm{next\\_prime}(p)$
- $p = \left\lfloor \frac{n}{q} \right\rfloor$
- 常规RSA解法
