from django.db import models

# Create your models here.
class Customer(models.Model):
    # id=models.IntegerField()
    name=models.CharField(max_length=40)
    address=models.CharField(max_length=50)
    age=models.IntegerField()
    mobileno=models.CharField(max_length=15, default='not available')
    
    def __str__(self):  #mandatory field
        return self.name
        
class Employee(models.Model):
    name=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    post=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Employee_1(models.Model):
    name=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    age=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    salary=models.CharField(max_length=50)
    designation=models.CharField(max_length=50)

    def __str__(self):
        return self.name



