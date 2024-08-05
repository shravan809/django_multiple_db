from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField(max_length=100)
    branch=models.CharField(max_length=100)

class Attendance(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    month=models.DateField()
    percentage=models.FloatField(max_length=100)

class Employee(models.Model):
    name=models.CharField(max_length=210)
    age=models.IntegerField()
    email=models.EmailField(max_length=100)
