from django.shortcuts import render

# Create your views here.
def learn_j(request):
    return render(request,'course/courseinfo.html')