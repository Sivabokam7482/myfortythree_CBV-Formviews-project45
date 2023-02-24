from django.shortcuts import render
from app1.forms import *
from django.views.generic import FormView
from django.http import HttpResponse
# Create your views here.

class student_form(FormView):
    template_name='data_formview.html'
    form_class=student

    def form_valid(self, form ):
        data=form.cleaned_data
        return HttpResponse(str(data))
    

class EmployData(FormView):
    template_name='data_Empform.html'
    form_class=Empform

    def form_valid(self,form):
        form.save()
        return HttpResponse('inserted data is successfully')

    









    





