from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPE =[
        ('admin', 'Admin'),
        ('viewer', 'Viewer'),
    ]
    user_type = models.CharField(max_length=50, choices=USER_TYPE)


class ResumeModel(models.Model):
    user = models.OneToOneField(CustomUser,null=True, on_delete=models.CASCADE)
    
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    designation = models.CharField(max_length=100, null=True)    
    contact_number = models.CharField(max_length=100, null=True)   
    age = models.CharField(max_length=50, null=True)    
    career_summary = models.CharField(max_length=100, null=True) 
    profile_pic = models.ImageField(upload_to="media/profile", max_length=100, null=True) 
    GENDER =[
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
        
    ]
    gender = models.CharField(choices=GENDER, max_length=200, null=True) 
    
    
    
    
    
    
    



