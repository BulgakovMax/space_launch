from django import forms


class LatinToCyrillicForm(forms.Form):
    LANGUAGE_CHOICES = [
    ('ru', 'Russian'),
    ('ua', 'Ukrainian'),
]
    my_text_input = forms.CharField(
        label=('Input your text'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 10})
    )
    my_language_choice = forms.ChoiceField(
        label=('Choose a language'),
        choices=LANGUAGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )