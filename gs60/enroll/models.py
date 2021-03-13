from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=543)
    desc=models.CharField(max_length=433)
    