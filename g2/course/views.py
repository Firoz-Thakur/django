from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def learn_django(request):
    cname='Djnago BABA'
    duration='37 years'
    seats='434'
    details={'x':cname,'y':duration,'z':seats}
    return render(request,'course/course1.html',context=details)


def learn_pyhton(request):
    return render(request,'course/course2.html')
