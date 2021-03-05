from django.shortcuts import render

# Create your views here.
from .form import stuReg

def showdata(request):
    fm=stuReg()
    return render(request,'enroll/userregistration.html',{'form':fm})

