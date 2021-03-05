from django import forms


class stuReg(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()