from django.urls import path

from .views import EmployeeListView, EmployeeCreateView, EmployeeDetailView, BranchCreateView, BranchListView, \
    EmployeeUpdateView, EmployeeDeleteView

app_name = "Employee"

urlpatterns = [
    path('employee/list/', EmployeeListView.as_view(), name="employee_list_view"),
    path('employee/create/', EmployeeCreateView.as_view(), name="employee_create_view"),
    path('employee/edit/<int:pk>/', EmployeeUpdateView.as_view(), name="employee_edit_view"),
    path('employee/delete/<int:pk>/', EmployeeDeleteView.as_view(), name="employee_delete_view"),
    path('employee/<int:pk>/', EmployeeDetailView.as_view(), name="employee_detail_view"),
    path('branch/create/', BranchCreateView.as_view(), name="branch_create_view"),
    path('branch/list/', BranchListView.as_view(), name="branch_list_view"),
]
