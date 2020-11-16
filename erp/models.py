from django.db import models

# Create your models here.
class Attendence(models.Model):

    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=30)
    semester=models.CharField(max_length=10)
    total_marks=models.IntegerField()
    obtained_marks=models.IntegerField()



class physics(models.Model):
    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=30)
    classes_conducted=models.CharField(max_length=30)
    classes_attended=models.CharField(max_length=30)
    total_marks=models.CharField(max_length=30)
    obtained_marks=models.CharField(max_length=30)

class chemistry(models.Model):
    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=30)
    classes_conducted=models.CharField(max_length=30)
    classes_attended=models.CharField(max_length=30)
    total_marks=models.CharField(max_length=30)
    obtained_marks=models.CharField(max_length=30)

class maths(models.Model):
    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=30)
    classes_conducted=models.CharField(max_length=30)
    classes_attended=models.CharField(max_length=30)
    total_marks=models.CharField(max_length=30)
    obtained_marks=models.CharField(max_length=30)

class english(models.Model):
    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=30)
    classes_conducted=models.CharField(max_length=30)
    classes_attended=models.CharField(max_length=30)
    total_marks=models.CharField(max_length=30)
    obtained_marks=models.CharField(max_length=30)

class computer(models.Model):
    name=models.CharField(max_length=100)
    usn=models.CharField(max_length=30)
    classes_conducted=models.CharField(max_length=30)
    classes_attended=models.CharField(max_length=30)
    total_marks=models.CharField(max_length=30)
    obtained_marks=models.CharField(max_length=30)








