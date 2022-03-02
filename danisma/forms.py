# -*- coding: utf-8 -*-
from django import forms
from danisma.models import Danisma

class DanismaFormu(forms.ModelForm):
    isim = forms.CharField(max_length=24, required=False, widget=forms.TextInput(attrs={'style': 'color:black;'}))
    mail = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'style': 'color:black;'}))
    metin = forms.CharField(required=True, max_length=10000, widget=forms.Textarea(attrs={'style': 'color:black;'}))

    class Meta:
        model = Danisma
        fields = ('isim', 'mail', 'metin')
        help_text = {
            'isim': None,
            'mail': None,
            'metin': None
        }