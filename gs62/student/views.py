from django.shortcuts import render

# Create your views here.

def setsession(request):
    return render(request,'student/setsession.html')
