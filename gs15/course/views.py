from django.shortcuts import render

# Create your views here.

def fees_django(request):
    return render(request,'course/course.html',{'title':'learn django','cname':'Django' })
