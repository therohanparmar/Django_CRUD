from django.contrib import admin
from CRUD_APP import models as CRUD_APP_Models

# Register your models here.

admin.site.register(CRUD_APP_Models.Employee),
admin.site.register(CRUD_APP_Models.Position),