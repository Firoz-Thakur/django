from django.shortcuts import render

# Create your views here.
from .form import stuReg

def showdata(request):
    fm=stuReg()
    return render(request,'enroll/userregistration.html',{'form':fm})

# auto_id : is use to remove the label and id in the html def get_context_data(self, **kwargs):
# label_suffix is used to remove the ':' from the Name :
# intitial : is used to give the intial value inside the input box
#order_field is used to change the order of the form fields
