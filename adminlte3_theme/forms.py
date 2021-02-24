from django import forms
from .models import confrence
class confrenceForm(forms.ModelForm):
    class Meta:
        model=confrence
        fields=('name','city','roll')
    