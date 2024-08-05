from django.contrib import admin
from django.urls import path
from .views import studentview,student_report,student_details_and_marks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',studentview,name='student'),
    path('student_details_and_marks/<int:hallticket>/', student_details_and_marks, name='student_details_and_marks'),
    path('report/<int:hallticket>',student_report,name='student_report'),
]