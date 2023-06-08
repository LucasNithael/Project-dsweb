from django import forms
from polls.models import Alternative


class RegisterAlter(forms.ModelForm):
    class Meta:
        model = Alternative
        fields = [
           'text',
        ]
        labels = {
            'text': 'Texto',
        }
        