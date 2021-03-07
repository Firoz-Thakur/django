from django.shortcuts import render
# Create your views here.
from .form import stuReg
from .models import user

def showdata(request):
    if request.method=='POST':
        fm=stuReg(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            obj=user(name=nm,email=em,password=pw)
            obj.save()
                                    
    else:
        fm=stuReg()

    return render(request,'enroll/u.html',{'form':fm})


