from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

image = CloudinaryField('image ')


class trek(models.Model):
    name = models.CharField(max_length=222)
    img = models.ImageField(upload_to='images',null=True,blank=True)
    level=models.CharField(max_length=222)
    ele = models.CharField(max_length=222)
    ime=models.CharField(max_length=222)


    description = models.TextField()
    
    def __str__(self):
        return self.name
    
class comment(models.Model):
    comment=models.CharField(max_length=50)
    

