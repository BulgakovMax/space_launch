from django.db.models import Count

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add rocket", 'url_name': 'add_page'},
        {'title': "Rockets", 'url_name': 'home'},
        {'title': "Locations", 'url_name': 'locations'},
        {'title': "Agencies", 'url_name': 'agencies'},
        {'title': "Contacts", 'url_name': 'contact'},
        ]


class DataMixin:
    paginate_by = 5

    def get_user_context(self, **kwargs):
        context = kwargs
        types = Type.objects.annotate(Count('rocket'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['types'] = types
        if 'type_selected' not in context:
            context['type_selected'] = 0
        return context
