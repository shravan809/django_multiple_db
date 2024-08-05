from django.shortcuts import render,redirect
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import Student,Reportcard
from .forms import StudentForm,ReportcardForm

def studentview(request):
    if request.method =='POST':
        fm=StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            message='student added successful'
    else:
        fm=StudentForm()
        message=''
    return render(request,'student.html',{'fm':fm,'message':message})

def student_details_and_marks(request, hallticket):
    #import pdb;pdb.set_trace()
    student = get_object_or_404(Student, hallticket=hallticket)
    reportcard = Reportcard.objects.filter(student=student).first()
    
    if request.method == 'POST':
        fm = ReportcardForm(request.POST, instance=reportcard)
        print(fm)
        if fm.is_valid():
            reportcard = fm.save(commit=False)
            reportcard.student = student
            reportcard.save()
            return redirect('student_report', hallticket=student.hallticket)
    else:
        fm = ReportcardForm(instance=reportcard)
        print(fm)
    return render(request, 'student_details_and_marks.html', {'student': student, 'fm': fm})


def student_report(request, hallticket):
    student = get_object_or_404(Student, hallticket=hallticket)
    reportcard = get_object_or_404(Reportcard, student=student)
    return render(request, 'reportcard.html', {'student': student, 'reportcard': reportcard})
