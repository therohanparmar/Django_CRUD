from django.shortcuts import render,redirect
from CRUD_APP import forms as CRUD_APP_FORMS
from CRUD_APP import models as CRUD_APP_Models
# Create your views here.


""" Get All Employee Details"""
def employee_list(request):
    context = {
        'employee_list':CRUD_APP_Models.Employee.objects.all()
    }
    return render(request, 'CRUD_APP/employee_list.html',context)

""" Insert-Update Operation"""
def employee_form(request,id=0):

    if request.method == 'GET':
        if id==0:
            form = CRUD_APP_FORMS.EmployeeForm
        else:
            employee = CRUD_APP_Models.Employee.objects.get(pk=id)
            form = CRUD_APP_FORMS.EmployeeForm(instance=employee)
        return render(request, 'CRUD_APP/employee_form.html',{'form':form})
    else:
        if id==0:
            form = CRUD_APP_FORMS.EmployeeForm(request.POST)
        else:
            employee = CRUD_APP_Models.Employee.objects.get(pk=id)
            form = CRUD_APP_FORMS.EmployeeForm(request.POST,instance=employee)
        if form.is_valid:
            form.save()
        return redirect('/employee/list')

""" Delete Employee """
def employee_delete(request,id):
    employee = CRUD_APP_Models.Employee.objects.get(pk=id)
    employee.delete()
    return redirect('/employee/list')