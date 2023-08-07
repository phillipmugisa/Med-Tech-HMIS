# Generated by Django 4.2 on 2023-05-13 00:39

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0002_alter_doctor_nin'),
        ('patients', '0009_generalfinding'),
    ]

    operations = [
        migrations.CreateModel(
            name='LabRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(blank=True, null=True, verbose_name='Updated on')),
                ('attendant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendant', to='doctor.doctor')),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='doctor.doctor')),
                ('visit', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='patients.visit')),
            ],
        ),
        migrations.CreateModel(
            name='LabTestCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='LabTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('price', models.DecimalField(blank=True, decimal_places=3, max_digits=9, null=True, verbose_name='Price')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(blank=True, null=True, verbose_name='Updated on')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_category', to='patients.labtestcategory')),
                ('request', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='patients.labrequest')),
            ],
        ),
    ]
