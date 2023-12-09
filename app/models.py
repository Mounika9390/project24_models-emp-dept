from django.db import models

# Create your models here.
class Dept(models.Model):
    dept_name=models.CharField(max_length=100)
    dept_no=models.PositiveBigIntegerField(primary_key=True)
    dept_loc=models.CharField(max_length=100)
    def __str__(self):
        return self.dept_name
    def __str__(self):
        return self.dept_no
    def __str__(self):
        return self.dept_loc
    
class Employee(models.Model):
    ename=models.CharField(max_length=100)
    empno=models.PositiveIntegerField(primary_key=True)
    job=models.CharField(max_length=100)
    def __str__(self):
        return self.ename
    def __str__(self):
        return self.empno
    def __str__(self):
        return self.job

class Salgrade(models.Model):
    grade=models.PositiveIntegerField()
    def __str__(self):
        return self.grade

