from django import forms
from .models import *


class AddPostForms(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = 'Категорія не обрана'
    class Meta:
        model = Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-input'}),
            'content' : forms.Textarea(attrs={'cols':60, 'rows':10}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise forms.ValidationError('Довжина перевищує 200 символів')

        return title