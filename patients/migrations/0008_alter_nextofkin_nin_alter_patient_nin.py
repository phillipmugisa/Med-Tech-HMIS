# Generated by Django 4.2 on 2023-05-12 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_remove_allergy_visit_allergy_patient'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextofkin',
            name='nin',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True, verbose_name='National Identification Number'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nin',
            field=models.CharField(blank=True, max_length=256, null=True, unique=True, verbose_name='National Identification Number'),
        ),
    ]