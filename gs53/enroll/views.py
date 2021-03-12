from django.shortcuts import render, HttpResponseRedirect
from .forms import Userform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import Userform
def sign_up(request):
    if request.method=="POST":
        fm=Userform(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=Userform()
    return render(request,'enroll/registration.html',{'form':fm})

def user_login(request):
   if not request.user.is_authenticated: 
       if request.method=="POST":
           fm=AuthenticationForm(request=request,data=request.POST)
           if fm.is_valid():
               uname=fm.cleaned_data['username']
               upass=fm.cleaned_data['password']
               user=authenticate(username=uname,password=upass)
               if user is not None:
                   login(request,user)
                   messages.success(request,"You have been successfully login ")
                   return HttpResponseRedirect('/profile/')
       else:
           fm=AuthenticationForm()
       return render(request,'enroll/login.html',{'form':fm})
   else:
        return HttpResponseRedirect('/profile/') 

def user_profile(request):
    if request.user.is_authenticated:
         return render(request,'enroll/profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')