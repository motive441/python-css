from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    roll = models.CharField(max_length=200)


    def __str__(self):
        return self.student_name


class Information(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.student.student_name