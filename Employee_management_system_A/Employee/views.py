from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import EmployeeForm, BranchForm
from .models import Employee, Branch, Designation


# Create your views here.


class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee_list.html"
    context_object_name = 'employee_list'
    permission_required = ('Employee.view_employee', 'Branch.view_branch')
    permission_denied_message = "You DoNot Have Necessary Permissions"


class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = "employee_edit.html"
    success_url = '/'


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    form_class = EmployeeForm
    success_url = '/'


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Employee
    fields = '__all__'
    template_name = "employee_create.html"
    permission_required = ('Employee.create_employee', 'Employee.view_employee', 'Branch.view_branch')
    permission_denied_message = "You DoNot Have Necessary Permissions"

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            form = EmployeeForm(request.POST, request.FILES)
            if form.is_valid():
                messages.add_message(request, messages.INFO, 'Employee added successfully !')
                form.save()
                return redirect("Employee:employee_create_view")
            else:
                context = {}
                context['error'] = form.errors
                context['form'] = form
                messages.add_message(request, messages.ERROR, 'Employee creation Failed!')
                return render(request, template_name="employee_create.html", context=context)
        else:
            render(request, template_name="employee_create.html")

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreateView, self).get_context_data(**kwargs)
        context['branch_list'] = Branch.objects.all()
        context['designation_list'] = Designation.objects.all()
        context['form'] = EmployeeForm()
        return context


class EmployeeDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    queryset = Employee.objects.select_related('designation', 'branch')
    model = Employee
    form_class = EmployeeForm
    template_name = "employee_details.html"
    context_object_name = 'employee_detail'
    permission_required = ('Employee.view_employee',)
    permission_denied_message = "You DoNot Have Necessary Permissions"


class BranchCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Branch
    fields = '__all__'
    template_name = 'branch_create.html'
    permission_required = ('Branch.create_branch', 'Branch.view_branch')
    permission_denied_message = "You DoNot Have Necessary Permissions"

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = BranchForm(request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.INFO, 'Branch added successfully !')
                return redirect("Employee:branch_list_view")
            else:
                context = {}
                context['error'] = form.errors
                context['form'] = form
                messages.add_message(request, messages.ERROR, 'Branch creation Failed!')
                return render(request, template_name="branch_create.html", context=context)
        else:
            render(request, template_name="branch_create.html")


class BranchListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Branch
    fields = '__all__'
    template_name = 'branch_list.html'
    context_object_name = 'branch_list'
    permission_required = ('Branch.crate_branch', 'Branch.view_branch')
    permission_denied_message = "You DoNot Have Necessary Permissions"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardView, self).get_context_data(**kwargs)
        employee_list = Employee.objects.all()
        context['employee_number'] = len(employee_list)
        context['branch_number'] = Branch.objects.all().count()
        context['designation_number'] = Designation.objects.all().count()
        context['employee_list'] = employee_list
        return context
