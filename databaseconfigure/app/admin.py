from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['name','age','email']

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','age','email']
