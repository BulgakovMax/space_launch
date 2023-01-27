from django.db.models import Count

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add article", 'url_name': 'add_page'},
        {'title': "Contacts", 'url_name': 'contact'},
        {'title': "Log in", 'url_name': 'login'}
        ]

class DataMixin:
    paginate_by = 20

    def get_user_context(self, **kwargs):
        context = kwargs
        types = Type.objects.annotate(Count('rocket'))

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu

        context['type'] = types
        if 'type_selected' not in context:
            context['type_selected'] = 0
        return context
