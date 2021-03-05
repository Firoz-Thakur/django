from django import forms

class stuReg(forms.Form):
    name=forms.CharField(label='Your name')  
    email=forms.EmailField(disabled=True)
    mobile=forms.IntegerField(initial='8987389',required=False)
    key=forms.CharField(widget=forms.HiddenInput())
    