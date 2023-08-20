from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=100)
    grade = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField()


