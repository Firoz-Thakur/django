from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def showdata(request):
    fm=UserForm()
    return render(request,'enroll/userregistration.html',{'form': fm })