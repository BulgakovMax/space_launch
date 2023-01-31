from django import forms
from .models import *


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
