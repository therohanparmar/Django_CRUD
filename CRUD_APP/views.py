from django.shortcuts import render

# Create your views here.


""" Get All Employee Details"""
def employee_list(request):
    return render(request, 'CRUD_APP/employee_list.html')

""" Insert-Update Operation"""
def employee_form(request):
    return render(request, 'CRUD_APP/employee_form.html')

""" Delete Employee """
def employee_delete(request):
    pass