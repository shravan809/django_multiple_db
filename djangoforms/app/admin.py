from django.contrib import admin
from .models import Student, Reportcard
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['hallticket','name','age','std']

@admin.register(Reportcard)
class ReportcardAdmin(admin.ModelAdmin):
    list_display=['student','telugu','hindi','english','maths','science','social','total','Avg','grade']