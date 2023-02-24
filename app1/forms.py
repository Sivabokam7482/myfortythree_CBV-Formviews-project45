from django import forms
from app1.models import *


class student(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()



class Empform(forms.ModelForm):
    class Meta:
        model=Employee
        fields='__all__'