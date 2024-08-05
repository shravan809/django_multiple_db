from django import forms
from .models import Student,Reportcard

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'

class ReportcardForm(forms.ModelForm):
    class Meta:
        model=Reportcard
        fields='__all__'