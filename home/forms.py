from django import forms
from home.models import Datastrore


class RegiForm(forms.ModelForm):
    post = forms.CharField(widget=forms.TextInput(attrs={

     'class': 'form-control' }
    ))

    class Meta:
        model = Datastrore
        fields = ('post',)
