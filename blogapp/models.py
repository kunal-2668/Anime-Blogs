from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.BigIntegerField()
    address = models.CharField(max_length=500)
    Time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    Title = models.CharField(max_length=40)
    # Choose_Image = models.ImageField(upload_to = 'images')
    Choose_Image = CloudinaryField('image')
    # Description = models.TextField(max_length=10000)
    Description = RichTextField(blank=True,null=True)
    Your_Name = models.CharField(max_length=40)
    time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(null=True,blank=True,default=False)

    class Meta:
      ordering = ['-time']

    def __str__(self):
        return self.Title

class Profile_photo(models.Model):
    user_name = models.CharField(max_length=255)
    profile = CloudinaryField('image')

    def __str__(self):
        return self.user_name



