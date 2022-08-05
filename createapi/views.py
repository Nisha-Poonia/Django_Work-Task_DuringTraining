from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from sms.models import Student
from  .serialiazer import StudentSerializer

# Create your views here.

# @api_view(['GET'])
@api_view(http_method_names=['GET','POST'])
def view_api(request):
    # resp=Response(data='This is my first api')
    res=3456
    res=3456.89
    res=[12,'hello',34.56]
    res=(34,45.6,'hello')
    res={3:'ram','hello':4,4:56}
    resp=Response(data=res)
    return resp
    
@api_view(['GET'])
def getstudentbyid(request,id):
    stu=Student.objects.get(id=id)
    stu_serialze=StudentSerializer(stu)
    resp=Response(data=stu_serialze.data)
    return resp

