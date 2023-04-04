from django.db.models import Count

from .models import *

menu = [{'title': "About", 'url_name': 'about'},
        {'title': "Add rocket", 'url_name': 'add_page'},
        {'title': "Rockets", 'url_name': 'home'},
        {'title': "Locations", 'url_name': 'locations'},
        {'title': "Agencies", 'url_name': 'agencies'},
        {'title': "Converter", 'url_name': 'convert_text'},
        {'title': "Contacts", 'url_name': 'contacts'},
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


def latin_to_cyrillic(text, language='ru'):
    if language == 'ru':
        latin_to_cyrillic_map = { 
        'a': 'ф', 'b': 'и', 'c': 'с', 'd': 'в', 'e': 'у', 'f': 'а',
        'g': 'п', 'h': 'р', 'i': 'ш', 'j': 'о', 'k': 'л', 'l': 'д',
        'm': 'ь', 'n': 'т', 'o': 'щ', 'p': 'з', 'q': 'й', 'r': 'к',
        's': 'ы', 't': 'е', 'u': 'г', 'v': 'м', 'w': 'ц', 'x': 'ч',
        'y': 'н', 'z': 'я', 'A': 'Ф', 'B': 'И', 'C': 'С', 'D': 'В',
        'E': 'У', 'F': 'А', 'G': 'П', 'H': 'Р', 'I': 'Ш', 'J': 'О',
        'K': 'Л', 'L': 'Д', 'M': 'Ь', 'N': 'Т', 'O': 'Щ', 'P': 'З',
        'Q': 'Й', 'R': 'К', 'S': 'Ы', 'T': 'Е', 'U': 'Г', 'V': 'М',
        'W': 'Ц', 'X': 'Ч', 'Y': 'Н', 'Z': 'Я', ';': 'ж', ':': 'Ж', 
        ',': 'б', '<': 'Б', '.': 'ю', ">": "Ю", "'": 'э', '"': "Є",
        '/': '.', '?': ',', ']': 'ъ', '}': 'Ъ', '[': 'х', '{': 'Х',
        '@': '"', '№': ';', ':': '^', '&': '?', 
    }
    elif language == 'ua':
        latin_to_cyrillic_map = {
        'a': 'ф', 'b': 'и', 'c': 'с', 'd': 'в', 'e': 'у', 'f': 'а',
        'g': 'п', 'h': 'р', 'i': 'ш', 'j': 'о', 'k': 'л', 'l': 'д',
        'm': 'ь', 'n': 'т', 'o': 'щ', 'p': 'з', 'q': 'й', 'r': 'к',
        's': 'і', 't': 'е', 'u': 'г', 'v': 'м', 'w': 'ц', 'x': 'ч',
        'y': 'н', 'z': 'я', 'A': 'Ф', 'B': 'И', 'C': 'С', 'D': 'В',
        'E': 'У', 'F': 'А', 'G': 'П', 'H': 'Р', 'I': 'Ш', 'J': 'О',
        'K': 'Л', 'L': 'Д', 'M': 'Ь', 'N': 'Т', 'O': 'Щ', 'P': 'З',
        'Q': 'Й', 'R': 'К', 'S': 'І', 'T': 'Е', 'U': 'Г', 'V': 'М',
        'W': 'Ц', 'X': 'Ч', 'Y': 'Н', 'Z': 'Я', ';': 'ж', ':': 'Ж', 
        ',': 'б', '<': 'Б', '.': 'ю', ">": "Ю", "'": 'є', '"': "Є",
        '/': '.', '?': ',', ']': 'ї', '}': 'Ї', '[': 'х', '{': 'Х',
        '@': '"', '№': ';', ':': '^', '&': '?', "\\": 'ґ', '|': 'Ґ',
        }
    translation_table = str.maketrans(latin_to_cyrillic_map)
    return text.translate(translation_table)