from django import template
from django.urls import resolve
from django.template import RequestContext
from django.utils.safestring import mark_safe

from menuapp.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name, parent_url=None):
    def draw_items(parent_item, items):
        menu_html = '<ul>'
        for item in items:
            active_class = ' class="active"' if context['request'].path == item.url else ''
            menu_html += f'<li{active_class}><a href="{"/menu/" + item.url}">' + item.name + '</a>'
            if item.children.exists():
                menu_html += draw_items(item, item.children.all())
            menu_html += '</li>'
        menu_html += '</ul>'
        return menu_html

    parent_url = list(context['request'].path.split("/"))[-2]
    menu_html = ''
    if parent_url == "menu":
        parent_items = MenuItem.objects.all()
        menu_items = []
        for x in parent_items:
            if x.parent:
                continue
            else:
                menu_items.append(x)

        parent_item = None
        menu_html = draw_items(parent_item, menu_items)
    elif parent_url:
        try:
            parent_item = MenuItem.objects.get(url=parent_url)
            menu_items = parent_item.children.all()
            menu_html = f'<h2> current menu is ' + parent_item.name + '</h2>'
            menu_html += draw_items(parent_item, menu_items)
        except MenuItem.DoesNotExist:
            parent_item = None
            menu_items = MenuItem.objects.none()
    else:
        parent_item = None
        menu_items = MenuItem.objects.filter(parent=None)
        menu_html = draw_items(parent_item, menu_items)

    return mark_safe(menu_html)
