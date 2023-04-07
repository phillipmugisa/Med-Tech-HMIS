# Generated by Django 4.2 on 2023-04-07 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_alter_nextofkin_patient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='relationship'),
        ),
    ]
