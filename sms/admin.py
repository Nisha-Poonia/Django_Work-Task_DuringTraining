from django.contrib import admin
from sms.models import*
# Register your models here.

# admin.site.register(Student)

# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#  list_display=['name','mobileno','address','pic','created_date']
 
#  admin.site.register(Employee)

# admin.site.register(Student)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','mobileno','address']