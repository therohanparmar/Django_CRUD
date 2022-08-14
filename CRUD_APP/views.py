from django.shortcuts import render
from CRUD_APP import forms as CRUD_APP_FORMS
# Create your views here.


""" Get All Employee Details"""
def employee_list(request):
    return render(request, 'CRUD_APP/employee_list.html')

""" Insert-Update Operation"""
def employee_form(request):
    form = CRUD_APP_FORMS.EmployeeForm
    return render(request, 'CRUD_APP/employee_form.html',{'form':form})

""" Delete Employee """
def employee_delete(request):
    pass