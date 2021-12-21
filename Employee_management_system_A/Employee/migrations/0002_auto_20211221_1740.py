# Generated by Django 3.2.9 on 2021-12-21 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Employee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='related_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='designation',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='auth.group'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='left_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]