from django.shortcuts import render
from .models import Student,Employee
from .forms import StudentForm,EmployeeForm
# Create your views here.
def student(request):
    stu = Student.objects.all()
    return render(request,'index.html', {'fm':stu})


def employee(request):
    emp=Employee.objects.using('secondary').all()
    return render(request, 'base.html',{'emp':emp})