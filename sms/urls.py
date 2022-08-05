from django.conf import settings
from django.urls import path
from.views import*
# from .import settings
# from django.conf.urls.static import static

 #http://127.0.0.1:8000/sms/

urlpatterns=[
    path('payment/',view_paymentsDetail),
    path('stu/',view_course_wise_student_detail),
    path('stufrm/',view_student),
    path('pay/',view_paymentdetail),
    path('empfrm/',view_employee),
    path('static/',view_static_files),
    path('detail/<int:sid>/',view_studetails), 
]                                                             