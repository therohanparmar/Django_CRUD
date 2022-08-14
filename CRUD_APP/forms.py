from dataclasses import field
import imp
from django import forms
from CRUD_APP import models as CRUD_APP_Models

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = CRUD_APP_Models.Employee
        fields = ['fullname','mobile_no','emp_code','position']
        labels = {
            'fullname':'Full Name',
            'mobile_no':'Mobile No.',
            'emp_code':'Employee Code',
            'position':'Position',
        }
    def __init__(self,*args,**kwargs):
        super(EmployeeForm,self).__init__(*args,**kwargs)
        self.fields['position'].empty_label = 'Select'