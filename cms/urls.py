from django.urls import path, re_path
from .views import*

urlpatterns=[
    path('home/',view_home),
    path('show/',view_show),
    path('marks20/',view_marks),
     path('table20/',view_dtl),
    path('prog1/',view_check),
    path('task1/', view_tskl),
    path('task2/', view_tsk2),
    path('task3/',view_tsk3),
    path('customer/',cms_view),
    path('employee/',ems_view)
]