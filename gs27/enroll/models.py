from django.db import models

# Create your models here.
class student(models.Model):
    stuid=models.IntegerField(max_length=59)
    stuname=models.CharField(max_length=95)
    stumail=models.EmailField(max_length=55)
    stupass=models.CharField(max_length=50)




    

