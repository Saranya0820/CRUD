from django.contrib import admin
from crudapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list = ['name','email','age','address','gender']

admin.site.register(Employee,EmployeeAdmin)
