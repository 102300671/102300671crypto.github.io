---
layout: home
title: Crypto
---

[源代码](https://github.com/102300671/102300671crypto.github.io/tree/main/_includes/code/nssctf)

{% for post in site.posts %}
{% assign file_components = post.path | split: '/' | last | split: '.' | first | split: '-' %}
{% assign year = file_components[0] %}
{% assign month = file_components[1] %}
{% assign day = file_components[2] %}
<p>{{ year }}-{{ month }}-{{ day }}</p>
<p><a href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></p>
{% endfor %}
