from django import template
from django.urls import resolve
from django.template import RequestContext
from django.utils.safestring import mark_safe

from menuapp.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.all()
    print(menu_name)
    print(menu_items)
    menu_html = '<ul>'
    for item in menu_items:
        menu_html += '<li>' + item.name
        if item.children.exists():
            menu_html += '<ul>'
            for child in item.children.all():
                menu_html += '<li>' + child.name + '</li>'
            menu_html += '</ul>'
        menu_html += '</li>'
    menu_html += '</ul>'
    return mark_safe(menu_html)
