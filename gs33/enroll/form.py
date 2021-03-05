from django import forms

class stuReg(forms.Form):
    name=forms.CharField(widget=forms.PasswordInput)  
    email=forms.EmailField(disabled=True)

   # name=forms.CharField(widget=forms.HiddenInput)
   # name=forms.CharField(widget=forms.Textarea)  
  #  name=forms.CharField(widget=forms.CheckboxInput) 
    name=forms.CharField(widget=forms.FileInput) 
    