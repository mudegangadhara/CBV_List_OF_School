from django.db import models

# Create your models here.
class School(models.Model):
    schoolname=models.CharField(max_length=100)
    schoolprincipal=models.CharField(max_length=100)
    schoollocation=models.CharField(max_length=100)
    def __str__(self):
        return self.schoolname
class Student(models.Model):
    school=models.ForeignKey(School,on_delete=models.CASCADE,related_name='Students')
    sid=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=100)
    sage=models.IntegerField()
    def __str__(self):
        return self.sname
