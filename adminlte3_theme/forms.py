from django import forms
from .models import confrence
class confrenceForm(forms.ModelForm):
    class Meta:
        model=confrence
        fields=('id','confrence_ID','date','venu','confrence_Overview','register','travel_information')
    