---
layout: default
title: Crypto-RSA(二)
math: true
math_type: svg
highlight: true
---

## nssctf

## [RSA2]P1

{% include_code nssctf/二/main1.py lang=python %}

n很小:

- 低加密指数攻击
- `m`可能满足$m^e<n$时有
- 此时$c=m^e$,$m=\sqrt(c,e)$(开方用`gmpy2`的`iroot`)
