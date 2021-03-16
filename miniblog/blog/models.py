from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=323)
    desc= models.TextField()
    photo=models.ImageField(upload_to="myimage")
    dat=models.DateTimeField(auto_now_add=True)
 #   hotel_Main_Img = models.ImageField(upload_to='images/') 