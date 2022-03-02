
from django import forms
from django.contrib.auth.models import User

class KayitFormu(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        help_texts = {
            'username': None
        }