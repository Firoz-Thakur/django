from django.shortcuts import render

# Create your views here.
from .form import stuReg

def showdata(request):
    fm=stuReg(auto_id='true',label_suffix=' ',initial={'name': 'Enter the Name','email':'Enter the email'})
    return render(request,'enroll/userregistration.html',{'form':fm})

# auto_id : is use to remove the label and id in the html def get_context_data(self, **kwargs):
# label_suffix is used to remove the ':' from the Name :
# intitial : is used to give the intial value inside the input box
