from django import forms
from .models import user
class stuReg(forms.ModelForm):
   class Meta:
      model=user
      fields=['name','email','password']
      labels={'name':'Enter your name bebi','password':'enter your password bebi','email':'enter the mail'}
      error_messages={
      'name':{'required':'Name likhna jaruri hein'},
       'password':{'required':'password likhna jaruri hein'}
      }
      widgets={'password' : forms.PasswordInput,'name':forms.TextInput(attrs={'class':'myfiroz','placeholder':'Yahn name likhiye'})}
   