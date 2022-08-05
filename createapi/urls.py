from django.urls import path 
from .views import*

# BASE URL:http://127.0.0.1.8000/api/

urlpatterns=[
    path('first/',view_api),
    path('student/<int:id>/',getstudentbyid)
]

