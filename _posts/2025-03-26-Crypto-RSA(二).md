---
layout: default
title: Crypto-RSA(二)
math: true
math_type: svg
---

## nssctf

## [RSA2]P1

{% highlight python linenos %}
{% include code/nssctf/2/main1.py %}
{% endhighlight %}

n很小:

- 低加密指数攻击
- `m`可能满足$m^e<n$时有
- 此时$c=m^e$,$\text{m}=\sqrt{c,e}$(开方用`gmpy2`的`iroot`)
