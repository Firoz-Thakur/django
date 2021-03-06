from django import forms

class stuReg(forms.Form):
   # name=forms.CharField(min_length=4,max_length=50,strip=True)  
   #  name=forms.CharField(error_messages={'required':'enter the name your baba'})
      name=forms.CharField()
      #agree=forms.BooleanField(label='I agree')
      password=forms.CharField(widget=forms.PasswordInput)
      rpassword=forms.CharField(widget=forms.PasswordInput)

      def clean(self):
         cleaned_data=super().clean()
         valpass=self.cleaned_data['password']
         valrpass=self.cleaned_data['rpassword']
         if valpass!=valrpass:
            raise forms.ValidationError('password not same baba')
         
    
    
    
    #  roll=forms.IntegerField(min_value=10,max_value=50)
   # name=forms.CharField(widget=forms.HiddenInput)
   # name=forms.CharField(widget=forms.Textarea)  
  #  name=forms.CharField(widget=forms.CheckboxInput) 
   # name=forms.CharField(widget=forms.FileInput) 
  
