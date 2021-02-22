from django.shortcuts import render

# Create your views here.
def fees_d(request):
    return render(request,'fees/fees1.html',{'nm':'djanog fuck'})
