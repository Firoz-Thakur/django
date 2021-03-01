from django.shortcuts import render
from datetime import datetime
from enroll.models import student
from django.db import models
# Create your views here.

def studentinfo(request):
    return render(request,'enroll/studetails.html',{'stu':student.objects.all()})