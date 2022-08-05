"""CetpaLiveProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))+

    
"""
from django.contrib import admin
from django.urls import path,include
from django.http import HttpResponse
from django.shortcuts import render


def add(request,a,b):
    print('Result: ',a+b)
    resp=HttpResponse("<h1>Hi i am calling sum function</h1>")
    return resp

def sub(request,a,b):
    print('Result: ',a-b)
    resp=HttpResponse("<h1>Hi i am calling sub function</h1>")
    return resp 

def mul(request,a,b):
    print('Result: ',a*b)
    resp=HttpResponse("<h1>Hi i am calling Multiply function</h1>")
    return resp   

def div(request,a,b):
    print('Result: ',a/b)
    resp=HttpResponse("<h1>Hi i am calling Divide function</h1>")
    return resp

def view_calc(request):
    resp=render(request,'calc11.html')
    return resp

def view_calc12(request):
    a=int(request.POST.get('t1',0))  
    b=int(request.POST.get('t2',0))
    # c=int(request.GET.get('t3','NA'))
    c=a+b
    print('a=',a,"b=",b,"sum=",c)
    resp=render(request,'calc12.html')
    return resp

def view_calc13(request):
    a=int(request.POST.get('t1',0))
    b=int(request.POST.get('t2',0))
    if request.method=='GET':
        resp=render(request,'calc13.html')
        return resp
    elif request.method=='POST':
        if 'btnsum' in request.POST:
            c=a+b
        elif 'btnsub' in request.POST:
            c=a-b
        elif 'btnmult' in request.POST:
            c=a*b
        elif 'btndiv' in request.POST:
            c=a/b
        d={'a':a,'b':b,'c':c}
        resp=render(request,'calc13.html',context=d)
        return resp

    # c=int(request.POST.get('t3',0))
    # c=a+b
    # d={'a':a,"b":b,"c":c}
    
    # print('a=',a,"b=",b,"sum=",c)
    # resp=render(request,'calc13.html',context=d)
    # return resp
def check_numeric_button(request):
    list_button=['btn1','btn2','btn3','btn4','btn5','btn6','btn7','btn8','btn9','btn0']
    for b in list_button:
        if b in request.POST:
            return b[3]
    return'-1'

def view_simple_calc(request):
    msg=request.POST.get('msg','')
    btn=check_numeric_button(request)
    if btn!="-1":
        msg+=btn
        d1={'msg':msg}
        resp=render(request,'calculator14.html',context=d1)
        return resp
    else:
        d1={'msg':msg}
        resp=render(request,'calculator14.html',context=d1)
        return resp
        
def view_calc14(request):
    a=int(request.POST.get('t1',0))
    b=int(request.POST.get('t2',0))
    if request.method=='GET':
        resp=render(request,'calc14.html')
        return resp
    elif request.method=='POST':
        if 'btn1' in request.POST:
           c=a+b  
        elif 'btnsub' in request.POST:
            c=a-b
        elif 'btnmult' in request.POST:
            c=a*b
        elif 'btndiv' in request.POST:
            c=a/b
        d={'a':a,'b':b,'c':c}
        resp=render(request,'calc14.html',context=d)
        return resp

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calc/sum/<int:a>/<int:b>',add),
    path('sub/<int:a>/<int:b>',sub),
    path('mul/<int:a>/<int:b>',mul),
    path('div/<int:a>/<int:b>',div),
    path('calculator/',view_calc),
    path('calculator12/',view_calc12),
    path('cms/',include('cms.urls')),     #http://127.0.0.1:8000/cms/
    path('sms/',include('sms.urls')),      #http://127.0.0.1:8000/sms/
    path('calculator13/',view_calc13),
    path('calculator14/',view_calc14),
    path('account/',include('account.urls')),   #http://127.0.0.1:8000/account/
    path('api/',include('createapi.urls')),
]