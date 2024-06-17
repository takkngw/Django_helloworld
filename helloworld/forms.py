from django import forms
from helloworld.models import Helloworld

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Helloworld
        fields = ('title', 'code', 'description')
