---
title: Category
layout: home
nav_order: 2
has_children: true
has_toc: false
---

## Categories

The phrases are divided into thematic categories. Choose  a category to get started. 


<center><p>
{% assign c = 0 %}
{% for row in site.data.categories %}
{% assign c = c | plus: 1 %}
<button type="button" name="button" class="btn-green" style="border: 0px;padding:5px;margin-right: 10px;" onclick="window.location.href='{% link {{row.name | prepend: "phrases/" }} %}';">{{row.short}}</button>
{% if c == 4 %}{% assign c=0 %}</p><p>{% endif %}
{% endfor %}
</p></center>

<br/><br/><br/><br/>