from django.shortcuts import render
# Create your views here.
from .models import user
from .form import stuReg

def showdata(request):
    if request.method=='POST':
        fm=stuReg(request.POST)
        if fm.is_valid():
          print("yeh post rquest hien")
          #print(fm.cleaned_data['agree'])
          nm=fm.cleaned_data['name']
          pw=fm.cleaned_data['password']
          em=fm.cleaned_data['email']
          obj=user(name=nm,email=em,password=pw)
         # obj=user(id=1,name=nm,email=em,password=pw) this way we can also update the value 
              # of particular field by mentioning the id(which is defalut given by django)
          obj=user(id=1)  #delete method
          obj.delete()                           
    else:
        fm=stuReg()

    return render(request,'enroll/u.html',{'form':fm})
