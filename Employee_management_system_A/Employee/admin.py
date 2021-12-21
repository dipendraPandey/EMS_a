from django.contrib import admin
from .models import Employee, Branch, Designation


# Register your models here.


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'address', 'contact_no')
    search_fields = ('full_name', 'designation')


class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_name', 'location', 'phone_no', ]
    search_fields = ['branch_name', 'location', ]


class DesignationAdmin(admin.ModelAdmin):
    list_display = ['id', 'designation']


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Designation, DesignationAdmin)
