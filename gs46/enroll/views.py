from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def regi(request):
    if request.method=="POST":
        fm=UserFrom(request.POST)
        if fm.isvalid():
            fm.save()
    else:
        fm=UserForm()
    return render(request,'enroll/userregistration.html',{'form':fm})   