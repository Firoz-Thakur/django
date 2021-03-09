from django.shortcuts import render
from .forms import UserForm
# Create your views here.
from django.contrib import messages

def regi(request):
    if request.method=="POST":
        fm=UserForm(request.POST)
        if fm.is_valid():
            fm.save()
           # messages.add_message(request,messages.SUCCESS,'Your account has been created')
            messages.success(request,'Your account has been created baba ji')
    else:
        fm=UserForm()
    return render(request,'enroll/userregistration.html',{'form':fm})

