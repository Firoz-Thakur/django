from django.db import models

class student(models.Model):
    stuid=models.IntegerField()
    stuname=models.CharField(max_length=63)
    stumail=models.EmailField(max_length=60)
    stupass=models.CharField(max_length=68) 



