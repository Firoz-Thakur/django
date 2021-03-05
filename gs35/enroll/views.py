from django.shortcuts import render

# Create your views here.
from .form import stuReg

def showdata(request):
    if request.method=='POST':
        fm=stuReg(request.POST)
        if fm.is_valid():
          print("yeh post rquest hien")
          print(fm)
          print('Name',fm.cleaned_data['name'])
          print('email',fm.cleaned_data['email'])
          print(fm.cleaned_data)
          fm=stuReg()   # used to just clean up the whole data
    else:
        fm=stuReg()
        print('ye get request hein')
    return render(request,'enroll/userregistration.html',{'form':fm})
