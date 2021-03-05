from django import forms

class stuReg(forms.Form):
    name=forms.CharField()  
    email=forms.EmailField()

   # name=forms.CharField(widget=forms.HiddenInput)
   # name=forms.CharField(widget=forms.Textarea)  
  #  name=forms.CharField(widget=forms.CheckboxInput) 
    #name=forms.CharField(widget=forms.FileInput) 
  
