from django.db import models

# Create your models here.
class student(models.Model):
    stuid=models.IntegerField(primary_key=True)
    stuname=models.CharField(max_length=70)
    stumail=models.EmailField(max_length=70)
    stupass=models.CharField(max_length=70)



