{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user }}
{% endblock %}

{% block html %}
<h4> Click link to activate your account.</h4>
{{token}}
{% endblock %}