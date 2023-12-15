from django.db import models
from django.contrib.auth.models import User

class course(models.Model):
    course_name=models.CharField(max_length=255)
    fee=models.IntegerField()
    
class student(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    student_age=models.IntegerField()
    student_name=models.CharField(max_length=255)
    student_address=models.CharField(max_length=255)
    joining_date=models.DateField()
    
class teacher(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    address=models.CharField(max_length=255)
    age=models.IntegerField()
    number=models.CharField(max_length=255)
    image=models.ImageField(upload_to="images/",null=True)
    
