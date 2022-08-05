from importlib.metadata import files
from django.http import HttpResponse
from django.shortcuts import render
from sms.forms import*
from sms.models import*



# Create your views here.   

def view_paymentsDetail(request):
    if request.method=='GET':
        resp=render(request,'sms/payment.html')
        return resp
    elif request.method=='POST':
        sid=int(request.POST.get('txtid',0))
        if Student.objects.filter(id=sid).exists():
            std=Student.objects.get(id=sid)
            allp=std.paymentdetails_set.all()
            d1={'payments':allp,'stu':std}
            resp=render(request,'sms/payment.html',context=d1)
            return resp
        else:
            d1={'msg':'No Payment Found!!'}
            resp=render(request,'sms/payment.html',context=d1)

def view_course_wise_student_detail(request):
    courses=Course.objects.all()
    d1={'courses':courses}
    if request.method =='GET':
        c=Course.objects.get(id=1)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'sms/student.html',context=d1)
        return resp
    elif request.method == 'POST':
        cid=int(request.POST.get('courses',0))
        c=Course.objects.get(id=cid)
        d1['cid']=c.id
        d1['cname']=c.name
        allstu=c.students.all()
        d1['students']=allstu
        resp=render(request,'sms/student.html',context=d1)
        return resp
        

def view_student(request):
    if request.method=='GET':
        frm_unbound=StudentForm()
        d1={'forms':frm_unbound}
        resp=render(request,'sms/studentfrm.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=StudentForm(request.POST,files=request.FILES)
        if frm_bound.is_valid():
         frm_bound.save()
         resp=HttpResponse("<h1>Student Added SuccessFully!!</h1>")
         return resp
        else:
            d1={'forms':frm_bound}
            resp=render(request,'sms/studentfrm.html',context=d1)
            return resp


def view_paymentdetail(request):
    if request.method=='GET':
        frm_unbound=PaymentDetailForm()
        d1={'Payment':frm_unbound}
        resp=render(request,'sms/paymentfrm.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=PaymentDetailForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=HttpResponse("<h1>Payment Added SuccessFully!!</h1>")
            return resp
        else:
            d1={'Payment':frm_bound}
            resp=render(request,'sms/paymentfrm.html',context=d1)
            return resp

def view_employee(request):
    if request.method=='GET':
        frm_unbound=EmployeeForm()
        d1={'employee':frm_unbound}
        resp=render(request,'sms/empfrm.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=EmployeeForm(request.POST)
        if frm_bound.is_valid():
            frm_bound.save()
            resp=HttpResponse("<h1>Employee Added SuccessFully!!</h1>")
            return resp
        else:
            d1={'employee':frm_bound}
            resp=render(request,'sms/empfrm.html',context=d1)
            return resp

def view_static_files(request):
    resp=render(request,'sms/demo.html')
    return resp

def view_studetails(request,sid):
    stu_details=Student.objects.get(id=sid)
    d1={'student':stu_details}
    resp=render(request,'sms/studetails.html',context=d1)
    return resp







    










