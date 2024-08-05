from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    dob=models.DateField()

class Book(models.Model):
    title=models.CharField(max_length=100)
    pub_date=models.DateField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    