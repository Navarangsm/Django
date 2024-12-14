from django import forms
from . models import person

class personForm(forms.ModelForm):
    class Meta:
            model = person
            fields = ['first_name','last_name','email','address']
        