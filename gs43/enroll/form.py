from django import forms
from .models import user
class stuReg(forms.ModelForm):
   name=forms.CharField(max_length=1000,required=False) #high priority
   class Meta:
      model=user
      fields=['name','email','password']
      labels={'name':'Enter your name bebi','password':'enter your password bebi','email':'enter the mail'}
      error_messages={
      'name':{'required':'Name likhna jaruri hein'},
       'password':{'required':'password likhna jaruri hein'}
      }
      widgets={'password' : forms.PasswordInput}
   