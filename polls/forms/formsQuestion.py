from django import forms
from polls.models import Question

class RegisterQuestion(forms.ModelForm):
    class Meta:
        model = Question
        fields = [
            'text',
        ]
        labels = {
            'text': 'Sua questão:',
        }