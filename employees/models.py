from django.db import models

# Create your models here.
class employee(models.Model):
    full_name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    phone = models.CharField(max_length=30,null=True)
    gender = models.CharField(max_length=30,null=True)
    post = models.CharField(max_length=30,null=True)
    salary = models.CharField(max_length=30,null=True)
    address = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)

class feedback(models.Model):
    full_name = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=True)
    massage = models.CharField(max_length=500,null=True)