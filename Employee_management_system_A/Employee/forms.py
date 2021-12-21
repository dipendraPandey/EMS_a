from django import forms

from .models import Employee, Branch


class TextInputWidget(forms.TextInput):
    attrs = {'class': "form-control"}

    class Media:
        pass


class DateInputWidget(forms.DateInput):
    attrs = {'class': "form-control", 'type': "date"}

    class Media:
        pass


class EmployeeForm(forms.ModelForm):
    join_date = forms.DateField(widget=forms.DateInput(attrs={'type': "date"}))
    left_date = forms.DateField(widget=forms.DateInput(attrs={'type': "date"}), required=False)
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': "form-control"}))
    passport_or_citizenship = forms.ImageField(widget=forms.FileInput(attrs={'class': "form-control"}))
    family_photo = forms.ImageField(widget=forms.FileInput(attrs={'class': "form-control"}), required=False)
    pan_no = forms.CharField(widget=forms.NumberInput())
    contact_no = forms.CharField(widget=forms.NumberInput())
    bio = forms.CharField(widget=forms.Textarea(), required=False)
    goods_provided = forms.CharField(required=False)

    class Meta:
        model = Employee
        fields = ['full_name', 'gender', 'address', 'designation', 'father_name', 'mother_name', 'join_date', 'branch',
                  'pan_no', 'contact_no', 'left_date', 'goods_provided', 'reference_by', 'bio', 'photo',
                  'passport_or_citizenship',
                  'family_photo']


class BranchForm(forms.ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'
