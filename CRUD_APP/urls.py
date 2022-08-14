
from django.contrib import admin
from django.urls import path,include
from CRUD_APP import views as CRUD_APP_Views

urlpatterns = [
    path('',CRUD_APP_Views.employee_form,name="Employee_Insert"),
    path('<int:id>/',CRUD_APP_Views.employee_form,name="Employee_Update"),
    path('list/',CRUD_APP_Views.employee_list,name="Employee_List"),
    path('delete/<int:id>/',CRUD_APP_Views.employee_delete,name="Employee_Delete"),
]
