from django import forms
from .models import *


class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['type'].empty_label = "Choose the type of rocket"

    class Meta:
        model = Rocket
        # fields = '__all__'
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 88, 'rows': 15}),
        }
