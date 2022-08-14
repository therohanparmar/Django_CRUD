from dataclasses import field
import imp
from django import forms
from CRUD_APP import models as CRUD_APP_Models

class EmployeeForm(forms.ModelForm):
    
    class Meta:
        model = CRUD_APP_Models.Employee
        fields = '__all__'