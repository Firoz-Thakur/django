from django import forms


class stuReg(forms.Form):
    name=forms.CharField()  
    email=forms.EmailField()
    first_name=forms.CharField() # will remove the underscore