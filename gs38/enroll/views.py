from django.shortcuts import render
# Create your views here.
from .form import stuReg

def showdata(request):
    if request.method=='POST':
        fm=stuReg(request.POST)
        if fm.is_valid():
          print("yeh post rquest hien")
          #print(fm.cleaned_data['agree'])
          print(fm.cleaned_data['name'])
          print(fm.cleaned_data['password'])
    else:
        fm=stuReg()

    return render(request,'enroll/u.html',{'form':fm})
