# Generated by Django 3.0.3 on 2020-02-23 08:22

import HackForms.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HackForms', '0004_merge_20200223_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='data',
        ),
        migrations.AlterField(
            model_name='project',
            name='csv_file',
            field=models.FileField(upload_to='E:\\projects\\HackFormsWeb\\media'),
        ),
        migrations.AlterField(
            model_name='project',
            name='empty_form',
            field=models.FileField(upload_to=HackForms.models.user_directory_path),
        ),
        migrations.AlterField(
            model_name='project',
            name='zip_file',
            field=models.FileField(upload_to=HackForms.models.user_directory_path),
        ),
    ]
