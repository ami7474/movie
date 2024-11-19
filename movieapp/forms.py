from django import forms

from .models import mlist


class movie1(forms.ModelForm):
    class Meta:
        model=mlist
        fields=['name','desc','year','img']

