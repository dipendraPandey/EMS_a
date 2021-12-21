from django.contrib.auth.models import Group, User
from django.db import models


# Create your models here.

def upload_location(instance, filename):
    file_path = 'Images/{name}/{filename}'.format(
        name=str(instance.full_name), filename=filename)
    return file_path


class Designation(models.Model):
    designation = models.CharField(max_length=120)
    group = models.ForeignKey(Group, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.designation


class Branch(models.Model):
    branch_name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    information = models.TextField(max_length=500, null=True, blank=True)
    phone_no = models.CharField(max_length=20)

    def __str__(self):
        return self.branch_name


class Employee(models.Model):
    related_user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='employee')
    full_name = models.CharField(max_length=150, blank=False)
    gender = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=150, blank=False)
    designation = models.ForeignKey(Designation, on_delete=models.PROTECT)
    father_name = models.CharField(max_length=150, blank=False)
    mother_name = models.CharField(max_length=150, blank=False)
    join_date = models.DateField(blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.PROTECT)
    pan_no = models.CharField(max_length=120, null=True)
    contact_no = models.CharField(max_length=20, blank=False)
    left_date = models.DateField(null=True, blank=True)
    goods_provided = models.CharField(max_length=200, null=True)
    reference_by = models.CharField(max_length=120, null=True)
    bio = models.TextField(max_length=500, null=True)
    photo = models.ImageField(upload_to=upload_location, blank=False)
    passport_or_citizenship = models.ImageField(upload_to=upload_location, blank=False)
    family_photo = models.ImageField(upload_to=upload_location, null=True, blank=True)

    def __str__(self):
        return self.full_name

    def delete(self, using=None, keep_parents=False):
        self.photo.storage.delete(self.photo.name)
        self.passport_or_citizenship.storage.delete(self.passport_or_citizenship.name)
        if self.family_photo:
            self.family_photo.storage.delete(self.family_photo.name)
        super().delete()
