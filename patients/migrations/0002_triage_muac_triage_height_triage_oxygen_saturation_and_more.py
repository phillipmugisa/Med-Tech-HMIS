# Generated by Django 4.2 on 2023-05-02 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='triage',
            name='MUAC',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='MUAC'),
        ),
        migrations.AddField(
            model_name='triage',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Height'),
        ),
        migrations.AddField(
            model_name='triage',
            name='oxygen_saturation',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Oxygen Saturation'),
        ),
        migrations.AddField(
            model_name='triage',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Weight'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='blood_pressure',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Blood Pressure'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='heart_rate',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Heart Rate'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='respiratory_rate',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Respiratory Rate'),
        ),
        migrations.AlterField(
            model_name='triage',
            name='temperature',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, verbose_name='Temperature'),
        ),
    ]