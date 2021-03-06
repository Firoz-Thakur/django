from django import forms

class stuReg(forms.Form):
   # name=forms.CharField(min_length=4,max_length=50,strip=True)  
   #  name=forms.CharField(error_messages={'required':'enter the name your baba'})
      name=forms.CharField(error_messages={'required': 'enter ur name bebi'})
      email=forms.EmailField(error_messages={'required': 'enter ur email'})
      password=forms.CharField(widget=forms.PasswordInput,error_messages={'required':'fuck Enter ur password'})
     


    
   