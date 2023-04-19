from django import template
from schedule.models import *

register = template.Library()

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add rocket", 'url_name': 'add_page'},
        {'title': "Agencies", 'url_name': 'agencies'}, 
        {'title': "Events", 'url_name': 'events_list'},
        {'title': "Launches", 'url_name': 'next_launch'},
        {'title': "Locations", 'url_name': 'locations'},
        {'title': "Rockets", 'url_name': 'home'},
        {'title': "Converter", 'url_name': 'convertor'},
        {'title': "Contacts", 'url_name': 'contacts'},
        {'title': "Log in", 'url_name': 'login'}
        ]


@register.simple_tag(name='gettypes')
def get_types(filter=None):
    if not filter:
        return Type.objects.all()
    else:
        return Type.objects.filter(pk=filter)


@register.inclusion_tag('schedule/list_categories.html')
def show_types(sort=None, type_selected=0):
    if not sort:
        type = Type.objects.all()
    else:
        type = Type.objects.order_by('title').values()

    return {'type': type, 'type_selected': type_selected}


@register.inclusion_tag('schedule/main_menu.html', takes_context=True)
def show_menu(context):
    request = context['request']
    user_menu = menu.copy()
    if not request.user.is_authenticated:
        user_menu.pop(1)
        return {'menu': user_menu}
    else:
        return {'menu': menu}

