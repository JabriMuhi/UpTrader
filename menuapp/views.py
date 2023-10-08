from django.shortcuts import render
from django.views import View

from menuapp.models import MenuItem


# def menu_view(request):
#     return render(request, 'menuapp/menu.html')
#


class MenuItemDetailView(View):
    template_name = 'menuapp/menu.html'

    def get(self, request, item_url=None):
        if item_url:
            try:
                parent_item = MenuItem.objects.get(url=item_url)
                children = parent_item.children.all()
            except MenuItem.DoesNotExist:
                parent_item = None
                children = None
        else:
            parent_item = None
            children = None

        context = {
            'parent_item': parent_item,
            'children': children,
        }

        return render(request, self.template_name, context)

