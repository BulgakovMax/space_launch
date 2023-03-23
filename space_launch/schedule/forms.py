from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import *
from django.utils.translation import gettext_lazy as _

LANGUAGE_CHOICES = (
    ('ru', _('Russian')),
    ('uk', _('Ukrainian')),
)

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Choose the type of rocket"
        self.fields['location'].empty_label = "Choose the launch location"
        self.fields['agency'].empty_label = "Choose the agency of rocket"

    class Meta:
        model = Rocket
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'type', 'location', 'agency']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 88, 'rows': 15}),
        }


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Log in', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class LatinToCyrillicForm(forms.Form):
    LANGUAGE_CHOICES = [
    ('ru', 'Russian'),
    ('ua', 'Ukrainian'),
]
    my_text_input = forms.CharField(
        label=_('Text Input'),
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    my_language_choice = forms.ChoiceField(
        label=_('Language'),
        choices=LANGUAGE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
