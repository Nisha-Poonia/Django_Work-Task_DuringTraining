from telnetlib import LOGOUT
from django.shortcuts import render
from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .decorator import check_authenticate

# Create your views here.
def view_home(request):
    resp=render(request,'account/home.html')
    return resp

@check_authenticate
def view_register(request):
    if request.method=='GET':
        frm_unbound=UserCreationForm()
        d1={'form':frm_unbound}
        resp=render(request,'account/register.html',context=d1)
        return resp
    elif request.method=='POST':
        frm_bound=UserCreationForm(request.POST)
        if frm_bound.is_valid():   #server side validation
            u=frm_bound.save()
            u.is_staff=True
            u.save()
            g1=Group.objects.get(name='StudentGroup')
            u.groups.add(g1)
            resp=HttpResponse("<h1> User Registered SuccessFully! </h1>")
            return resp
        else:
            d1={"form":frm_bound}
            resp=render(request,'account/register.html',context=d1)
            return resp

@check_authenticate
def view_login(request):
    if request.method=='GET':
        resp=render(request,'account/login.html')
        return resp
    elif request.method=='POST':
        u_user=request.POST.get('txtusername','')
        u_pass=request.POST.get('txtpassword','')
        u=authenticate(request=request,username=u_user,password=u_pass)
        print("user:",u)
        if u is not None:
            login(request,user=u)
            # resp=HttpResponse("<h1>Login SuccessFully!!</h1>")
            resp=render(request,'account/home.html')
            return resp
        else:
            # resp=HttpResponse("<h1> Login Failed!!</h1>")
            resp=render(request,'account/login.html')
            return resp


def view_logout(request):
    logout(request=request)
    resp=render(request,'account/logout.html')
    return resp

@login_required(login_url='login')
def view_secure1(request):
    resp=render(request,'account/secure1.html')
    return resp

@login_required(login_url='login')
def view_secure2(request):
    resp=render(request,'account/secure2.html')
    return resp

def view_unsecure1(request):
    resp=render(request,'account/unsecure1.html')
    return resp

def view_unsecure2(request):
    resp=render(request,'account/unsecure2.html')
    return resp