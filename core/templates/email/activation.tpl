{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ user }}
{% endblock %}

{% block html %}
<h4> Click link to activate your account.</h4>
<a>http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{token}}/</a>
{% endblock %}