from django.contrib import admin
from CRUD_APP import models as CRUD_APP_Models

# Register your models here.

class EmloyeeAdmin(admin.ModelAdmin):
    list_display = ['fullname','emp_code','mobile_no','position']
admin.site.register(CRUD_APP_Models.Employee,EmloyeeAdmin),
admin.site.register(CRUD_APP_Models.Position),