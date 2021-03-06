from django import forms

class stuReg(forms.Form):
   # name=forms.CharField(min_length=4,max_length=50,strip=True)  
   #  name=forms.CharField(error_messages={'required':'enter the name your baba'})
      name=forms.CharField()
      #agree=forms.BooleanField(label='I agree')
      password=forms.CharField(widget=forms.PasswordInput)


      def clean(self):
         cleaned_data=super().clean()
         valname=self.cleaned_data['name']
         valpass=self.cleaned_data['password']
         
         if len(valpass)<4:
            raise forms.ValidationError('enter password more than or equal to 4 char')
         if len(valname)<7:
            raise forms.ValidationError('enter the name more than or equal to 7 char')
    
    
    
    
    #  roll=forms.IntegerField(min_value=10,max_value=50)
   # name=forms.CharField(widget=forms.HiddenInput)
   # name=forms.CharField(widget=forms.Textarea)  
  #  name=forms.CharField(widget=forms.CheckboxInput) 
   # name=forms.CharField(widget=forms.FileInput) 
  
