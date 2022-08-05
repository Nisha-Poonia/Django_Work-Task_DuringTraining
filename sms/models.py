from django.db import models


# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    address=models.TextField()
    mobileno=models.CharField(max_length=15)
    pic=models.ImageField(null=True,blank=True)
    dateofbirth=models.DateField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    last_update_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

class Course(models.Model):
    name=models.CharField(max_length=50)
    students=models.ManyToManyField(Student,null=True,blank=True)
    def __str__(self):
        return self.name

class PaymentDetails(models.Model):
    amount=models.IntegerField() 
    payment_mode=models.CharField(max_length=50,choices=[('payTm','payTm'),('Debit Card','Debit Card'),('Credit Card','Credit Card'),('cash','cash')])
    payment_date=models.DateTimeField(auto_now=True)
    student=models.ForeignKey(Student,null=False,blank=False,on_delete=models.CASCADE)
    def __str__(self):
        return self.amount

ch=(('delhi','Delhi'),('noida','Noida'),('hisar','Hisar'),('rohtak','Rohtak'))
class Employee(models.Model):
    name=models.CharField(max_length=50,null=False,blank=False)
    address=models.TextField()
    city=models.CharField(max_length=6,choices=ch,default='delhi')
    age=models.CharField(max_length=15)
    salary=models.CharField(max_length=50,null=False,blank=False)
    def __str__(self):
        return self.name


