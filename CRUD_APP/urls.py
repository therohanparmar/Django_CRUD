
from django.contrib import admin
from django.urls import path,include
from CRUD_APP import views as CRUD_APP_Views

urlpatterns = [
    path('',CRUD_APP_Views.employee_form),
    path('list/',CRUD_APP_Views.employee_list),
]
