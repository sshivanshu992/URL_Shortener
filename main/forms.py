from django import forms
from .models import Shortner

class ShortnerForm(forms.ModelForm):
    url =  forms.URLField(widget=forms.URLInput(attrs={'class':'form-control bg-white y-height', 'placeholder' : 'Shorten your link'} ), required=True, label='')

    class Meta:
        model = Shortner
        fields = ['url']