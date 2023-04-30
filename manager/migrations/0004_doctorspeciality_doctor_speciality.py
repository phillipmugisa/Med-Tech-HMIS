# Generated by Django 4.2 on 2023-04-07 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorSpeciality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ManyToManyField(related_name='doctor_speciality', to='manager.doctorspeciality'),
        ),
    ]