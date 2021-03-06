from django import forms

class stuReg(forms.Form):
   # name=forms.CharField(min_length=4,max_length=50,strip=True)  
   #  name=forms.CharField(error_messages={'required':'enter the name your baba'})
      email=forms.EmailField(empty_value='fiorzbhaikar21@gmail.com')
      agree=forms.BooleanField(label='I agree')
      price=forms.DecimalField(min_value=10,max_value=50, max_digits=4,decimal_places=1)

    #  roll=forms.IntegerField(min_value=10,max_value=50)
   # name=forms.CharField(widget=forms.HiddenInput)
   # name=forms.CharField(widget=forms.Textarea)  
  #  name=forms.CharField(widget=forms.CheckboxInput) 
   # name=forms.CharField(widget=forms.FileInput) 
  
