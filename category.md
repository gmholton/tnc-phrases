---
title: Category
layout: home
nav_order: 2
has_children: true
has_toc: false
---

## Categories

The phrases are divided into thematic categories. Choose  a category to get started. 


<div style="display:flex;align-items:center;flex-wrap:wrap;margin-left:25px;margin-right:25px;">
{% for row in site.data.categories %}
<div style="margin:10px;">
<button type="button" name="button" class="btn-green" style="border-radius:5px;border: 0px;padding-top:5px;padding-bottom:5px;padding-left:10px;padding-right:10px;" onclick="window.location.href='{% link {{row.name | prepend: "phrases/" }} %}';">{{row.short}}</button>
</div>
{% endfor %}
</div>

<br/><br/><br/><br/>