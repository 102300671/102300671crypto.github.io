---
layout: home
---

{% for post in site.posts %}
{% assign file_components = post.path | split: '/' | last | split: '.' | first | split: '-' %}
{% assign year = file_components[0] %}
{% assign month = file_components[1] %}
{% assign day = file_components[2] %}
<p>{{ year }}-{{ month }}-{{ day }}</p>
<p><a href="{{site.baseurl}}{{ post.url }}">{{ post.title }}</a></p>
{% endfor %}
