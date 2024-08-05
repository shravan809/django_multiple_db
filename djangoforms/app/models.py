from django.db import models

# Create your models here.
class Student(models.Model):
    hallticket=models.IntegerField(default=100)
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    std=models.CharField(max_length=100)

class Reportcard(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    telugu=models.FloatField()
    hindi=models.FloatField()
    english=models.FloatField()
    maths=models.FloatField()
    science=models.FloatField()
    social=models.FloatField()
    total = models.FloatField(editable=False, default=0)
    Avg = models.FloatField(editable=False, default=0)
    grade = models.CharField(max_length=5, editable=False, default='')

    def save(self, *args, **kwargs):
        self.total = sum([
            self.telugu, self.hindi, self.english,
            self.maths, self.science, self.social
        ])
        self.Avg = self.total / 6

        if self.Avg >= 90:
            self.grade = 'A'
        elif self.Avg >= 80:
            self.grade = 'B'
        elif self.Avg >= 70:
            self.grade = 'C'
        elif self.Avg >= 60:
            self.grade = 'D'
        else:
            self.grade = 'F'

        super().save(*args, **kwargs)
    