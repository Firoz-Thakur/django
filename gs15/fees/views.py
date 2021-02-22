from django.shortcuts import render

# Create your views here.
def learn_django(request):
    return render(request,'fees/fees.html',{'title':'fees django','cname':'django' ,'charge':300})
