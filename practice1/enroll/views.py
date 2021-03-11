from django.shortcuts import render
from .forms import UserForm
from django.contrib import messages
# Create your views here.
def UserRegistration(request):
    if request.method=="POST":
         fm=UserForm(request.POST)
         if fm.is_valid:
             fm.save()
             messages.success(request,"You have successfully created your account")
    else:  
         fm=UserForm()
    return render(request,'enroll/registration.html',{'form':fm})

