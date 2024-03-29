# Generated by Django 4.2 on 2023-05-15 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lab', '0002_assignedtest_labtest_subtest_subtestresult_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Name')),
            ],
        ),
        migrations.AddField(
            model_name='request',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='request_category', to='lab.testcategory'),
            preserve_default=False,
        ),
    ]
