# Generated by Django 4.2 on 2023-04-07 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NextOfKin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=256, verbose_name='First Name')),
                ('middlename', models.CharField(blank=True, max_length=256, null=True, verbose_name='Middle Name')),
                ('lastname', models.CharField(max_length=256, verbose_name='Last Name')),
                ('nin', models.CharField(max_length=256, verbose_name='National Identification Number')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=256, verbose_name='Gender')),
                ('telnumber', models.CharField(max_length=256, verbose_name='Phone Number')),
                ('alttelnumber', models.CharField(blank=True, max_length=256, null=True, verbose_name='Alternative Phone Number')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=256, null=True, verbose_name='Address')),
                ('slug', models.SlugField(blank=True, max_length=200, null=True, unique=True, verbose_name='Safe Url')),
                ('created_on', models.DateField(blank=True, null=True, verbose_name='Updated on')),
                ('relationship', models.CharField(max_length=256, verbose_name='relationship')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
