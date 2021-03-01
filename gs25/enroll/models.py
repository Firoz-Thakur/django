from django.db import models

# Create your models here.
class student(models.Model):
 stuid=models.IntegerField(max_length=40)
 stuname=models.CharField(max_length=40)
 stumail=models.EmailField(max_length=40)
 stupass=models.IntegerField(max_length=40)

def __str__(self):
    return str(self.stuid)

 