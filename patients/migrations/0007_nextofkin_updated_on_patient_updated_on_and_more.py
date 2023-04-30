# Generated by Django 4.2 on 2023-04-07 20:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_visit_patient_patient_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='nextofkin',
            name='updated_on',
            field=models.DateField(blank=True, null=True, verbose_name='Updated on'),
        ),
        migrations.AddField(
            model_name='patient',
            name='updated_on',
            field=models.DateField(blank=True, null=True, verbose_name='Updated on'),
        ),
        migrations.AlterField(
            model_name='nextofkin',
            name='created_on',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Created on'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='created_on',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Created on'),
        ),
    ]