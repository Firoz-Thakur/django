from django.shortcuts import render
from enroll.models import student
# Create your views here.

def studentinfo(request):
    name=student.objects.all()
    return render(request,'enroll/studetail.html',{'stu' : name})
    