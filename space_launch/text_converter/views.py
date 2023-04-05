from django.shortcuts import render
from .forms import LatinToCyrillicForm
from .utils import latin_to_cyrillic


def convertor(request):
    form = LatinToCyrillicForm()
    translated_text = ''
    if request.method == 'POST':
        form = LatinToCyrillicForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('my_text_input')
            language = form.cleaned_data.get('my_language_choice')
            # Split text into lines and translate each line separately
            translated_lines = []
            for line in text.split('\n'):
                translated_lines.append(latin_to_cyrillic(line.strip(), language))
            # Join translated lines back into a single string with line breaks
            translated_text = '\n'.join(translated_lines)
    context = {'form': form, 'translated_text': translated_text}
    return render(request, 'text_converter/convert_text.html', context)
