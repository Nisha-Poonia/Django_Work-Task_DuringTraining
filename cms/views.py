from genericpath import exists
from math import factorial
from re import A, X
from django.shortcuts import render
from django.http import HttpResponse
from cms.models import Customer
from cms.models import Employee_1
from cms.models import Employee


# Create your views here.

def view_home(request):
    # resp=HttpResponse("<h1>Hello WELCOME TO CMS</h1>")
    # return resp
    resp=render(request,'cms/home.html')
    return resp

def view_show(request):
    # resp=HttpResponse("<h1>Show ALL Customer</h1>")
    # return resp
    resp=render(request,'cms/show.html')
    return resp

def view_check(request):
    # d1={'ch':'p'}
    d1={ 'a':20, 'b':45, 'c':23}
    resp=render(request,'cms/prog1_19.html',context=d1)
    return resp

def view_marks(request):
    if request.method=='GET':
        resp=render(request,'cms/marks20.html')
        return resp
    elif request.method=='POST':
        a=int(request.POST.get('physics',0))
        b=int(request.POST.get('chemistry',0))
        c=int(request.POST.get('math',0))
        d=int(request.POST.get('hindi',0))
        e=int(request.POST.get('english',0))
        res= ( a + b + c + d + e)
        print(res)
        res_p=(a+b+c+d+e)/5
        # res=request.POST.get("t3")
        if res_p >= 90 :
            per="Grade S"
        elif res_p >= 80 and res_p<90:
            per="Grade A"
        elif res_p>=70 and res_p<80:
            per="Grade B"
        elif res_p>=60 and res_p<70:
            per="Grade C"
        elif res_p>=50 and res_p<60:
            per="Grade D"
        else:
            per="FAIL"

        d1={'res':res, 'res_p':res_p,'per':per}
        resp =render(request,'cms/marks20.html',context=d1)
        return resp

# def task1_20(request):
#     if request.method=='GET':
#         resp=render(request,'cms/task1_20.html')
#         return resp
    
#     elif request.method=='POST':
#         num1=dict()
#         number=int(request.POST.get('num'))
#         for i in range(1,11):
#             num1[i]=number*i
#             return num1[i]

# class Employee:
#     def __init__(self):
#         self.id=0
#         self.name=''
#         self.age=0
#         self.city=''

def view_dtl(request):
        employee=get_N_Employee(10)
        d1={'employee':employee}
        resp=render(request,'cms/table20.html',context=d1)
        return resp

    
def get_N_Employee(n):
    list_emp=[]
    for i in range(1,n+1):
        emp=Employee()
        emp.id="ID"+str(i)
        emp.name="Name"+str(i)
        emp.age="Age"+str(i)
        emp.city="City"+str(i)
        list_emp.append(emp)
    return list_emp

class Task1:
    def __init__(self):
        self.expression=''
        self.result=0

# def get_N_Expression(input):
#     list_expression=[]
#     for i in range(1,11):
#         tsk1=Task1()
#         tsk1.expression=str(input)+'*' + str(i)
#         list_expression.append(tsk1)
#     return list_expression

def view_result(num):
        list_result=[]
        for i in range(1,11):
            num1 = Task1()
            num1.result=num*i
            list_result.append(num1)
        return list_result
            
    
def view_tskl(request):
    input=int(request.POST.get('t',0))
    # exp=get_N_Expression(input)
    res=view_result(input)
    d1={'input':input,'res':res}
    resp=render(request,'cms/task1_20.html',context=d1)
    return resp

def view_task2(num):
    fact = 1
    if num == 0  or num == 1:
        fact=1
    else:
        fact=num*view_task2(num-1)
    return fact

def view_tsk2(request):
    if request.method=='GET':
        resp=render(request,'cms/task2_20.html')
        return resp
    elif request.method=='POST':
        num=int(request.POST.get('t1',0))
        res=view_task2(num)
        # print(res)
        d1={'res':res}
        resp=render(request,'cms/task2_20.html',context=d1)
        return resp

def view_task3(a,b):
    if b==0 :
        return a
    else:
       return view_task3(b,a%b)

def view_task3lcm(a,b):
    if a > b:
       greater=a
    else:
        greater=b

    while(True):
        if((greater % a == 0) and (greater % b == 0)):
            lcm = greater
            break
        greater = greater+1
    return lcm
       
def view_tsk3(request):
    if request.method=='GET':
        resp=render(request,'cms/task3_20.html')
        return resp
        
    elif request.method=='POST':
        a=int(request.POST.get('t1',0))
        b=int(request.POST.get('t2',0))
        lcm=view_task3lcm(a,b)
        gcd=view_task3(a,b)
        # print(res)
        d1={'res':gcd,'lcm':lcm}
        resp=render(request,'cms/task3_20.html',context=d1)
        return resp

def cms_view(request):
    if request.method=='GET':
        resp=render(request,'cms/cms_25.html')
        return resp
    elif request.method=='POST':
        if 'btnadd' in request.POST:
            cus=Customer()
            cus.name=request.POST.get('textname','NA')
            cus.address=request.POST.get('textaddress','NA')
            cus.age=int(request.POST.get('textage',0))
            cus.mobileno=request.POST.get('textmob','NA')
            cus.save()
            resp=HttpResponse("<h1> Customer Added SuccessFully!! whose ID : "+str(cus.id)+"</h1>")
            return resp
        elif 'btnsearch' in request.POST:
            cusid=int(request.POST.get('textcusid',0))
            cus=Customer.objects.get(id=cusid)
            d1={'cus':cus}
            resp=render(request,'cms/cms_25.html',context=d1)
            return resp 
        elif 'btnupdate' in request.POST:
            cus=Customer()
            cus.id=int(request.POST.get('textcusid',0))
            if Customer.objects.filter(id=cus.id).exists():
                cus.name=request.POST.get('textname','NA')
                cus.address=request.POST.get('textaddress','NA')
                cus.age=int(request.POST.get('textage','0'))
                cus.mobileno=request.POST.get('textmob','NA')
                cus.save()
                resp=HttpResponse("<h1> Customer Update SuccessFully!! whose ID : "+str(cus.id)+"</h1>")
                return resp

        elif 'btndelete' in request.POST:
            cus=Customer()
            cus.id=int(request.POST.get('textcusid',0))
            Customer.objects.filter(id=cus.id).delete()
            resp=HttpResponse("<h1>Customer Deleted SuccessFully!! whose ID : "+str(cus.id)+"</h1>")
            return resp

        elif 'btnshow' in request.POST:
            allcus=Customer.objects.all()
            d1={'allcus':allcus}
            resp=render(request,'cms/cms_25.html',context=d1)
            return resp


def ems_view(request):
    if request.method=='GET':
        resp=render(request,'cms/ems_26.html')
        return resp
    elif request.method=='POST':
        if 'btnadd' in request.POST:
            emp=Employee_1()
            emp.name=request.POST.get('textname','NA')
            emp.address=request.POST.get('textaddress','NA')
            emp.age=int(request.POST.get('textage',0))
            emp.city=request.POST.get('textcity','NA')
            emp.salary=int(request.POST.get('textsalary',0))
            emp.designation=request.POST.get('textdesig','NA')
            emp.save()
            resp=HttpResponse("<h1> Employee Added SuccessFully!! whose ID : "+str(emp.id)+"</h1>")
            return resp
        elif 'btnsearch' in request.POST:
            empid=int(request.POST.get('textempid',0))
            emp=Employee_1.objects.get(id=empid)
            d1={'emp':emp}
            resp=render(request,'cms/ems_26.html',context=d1)
            return resp 
        elif 'btnupdate' in request.POST:
            emp=Employee_1()
            emp.id=int(request.POST.get('textempid',0))
            if Employee_1.objects.filter(id=emp.id).exists():
                emp.name=request.POST.get('textname','NA')
                emp.address=request.POST.get('textaddress','NA')
                emp.age=int(request.POST.get('textage','0'))
                emp.city=request.POST.get('textcity','NA')
                emp.salary=int(request.POST.get('textsalary',0))
                emp.designation=request.POST.get('textdesig','NA')
                emp.save()
                resp=HttpResponse("<h1> Employee Update SuccessFully!! whose ID : "+str(emp.id)+"</h1>")
                return resp

        elif 'btndelete' in request.POST:
            emp=Employee_1()
            emp.id=int(request.POST.get('textempid',0))
            Employee_1.objects.filter(id=emp.id).delete()
            resp=HttpResponse("<h1>Employee Deleted SuccessFully!! whose ID : "+str(emp.id)+"</h1>")
            return resp

        elif 'btnshow' in request.POST:
            allemp=Employee_1.objects.all()
            d1={'allemp':allemp}
            resp=render(request,'cms/ems_26.html',context=d1)
            return resp



                
                