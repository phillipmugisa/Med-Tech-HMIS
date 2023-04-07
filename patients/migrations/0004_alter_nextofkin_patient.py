# Generated by Django 4.2 on 2023-04-07 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0003_nextofkin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextofkin',
            name='patient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nextOfKin', to='patients.patient'),
        ),
    ]
