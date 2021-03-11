from django.shortcuts import render

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


