import math

from django import template
from django.template import engines
from django.utils.html import format_html
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter
def get_flag(obj, attr):
    return obj[attr]


@register.simple_tag
def tuple_args(dictionary, a, b):
    if (a, b) in dictionary.keys():
        return math.sqrt(dictionary[(a, b)]/1000000000)
    else:
        return 0


@register.filter()
def get_value(dictionary, key):
    if key in dictionary.keys():
        return int(10 * float(dictionary.get(key)))
    else:
        return 0


@register.filter()
def nbsp(value):
    if value:
        return mark_safe("&nbsp;".join(value.split(' ')))
    else:
        pass


@register.filter()
def slugify(value):
    tmp = value.lower()
    tmp = tmp.replace(" ", "_")
    return tmp


@register.filter()
def deslugify(value):
    tmp = value.replace("_", " ")
    return tmp


# INSTEAD OF {{ page.content | safe }}
@register.simple_tag()
def render_doc_page(value):
    django_engine = engines['django']
    my_template = django_engine.from_string(value)
    rendered = my_template.render()
    return rendered


# render a link to the Open Risk Manual
@register.simple_tag()
def orm(url, name):
    url_text = format_html('<a href="https://www.openriskmanual.org/wiki/' + url + '">' + name + '</a>')
    return url_text


# render a link to the Open Risk Blog
@register.simple_tag()
def blog(url, name):
    url_text = format_html('<a href="https://www.openriskmanagement.com/' + url + '">' + name + '</a>')
    return url_text


@register.filter()
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter()
def get_list_item(List, i):
    if i < len(List):
        return List[int(i)]
    else:
        return List[0]


@register.filter()
def significant_figures(x, s):
    return round(x, s)
