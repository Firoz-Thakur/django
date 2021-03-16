from django.shortcuts import render

# Create your views here.
def setcookie(request):
    reponse=render(request,'student/setcookie.html')
    reponse.set_cookie('name','sonam')
    return reponse


