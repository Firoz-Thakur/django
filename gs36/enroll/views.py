from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .form import stuReg

def thankyou(request):
    return render(request,'enroll/success.html')

def showdata(request):
    if request.method=='POST':
        fm=stuReg(request.POST)
        if fm.is_valid():
          print("yeh post rquest hien")
          print(fm)
          print('Name',fm.cleaned_data['name'])
          print('email',fm.cleaned_data['email'])
          print(fm.cleaned_data)
          return HttpResponseRedirect('/reg/success/')
         # return render(request,'enroll/success.html',{'nm':fm.cleaned_data['name']})
            #render to other page so that the form get cleaned
    else:
        fm=stuReg()
        print('ye get request hein')
    return render(request,'enroll/userregistration.html',{'form':fm})
