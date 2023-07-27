from django import forms
from.models import * 

class trekform(forms.ModelForm):
    class Meta:
        model=trek
        fields='__all__'


class commentform(forms.ModelForm):
    class Meta:
        model=comment
        fields='__all__'