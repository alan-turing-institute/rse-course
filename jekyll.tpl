{%- extends 'basic.tpl' -%}
{%- block header -%}
---
title: {% if 'jekyll' in nb['metadata'] %} {{nb['metadata']['jekyll']['display_name']}} {% endif %}
nblink: True
---
{{super()}}
{%- endblock header -%}

