# Generated by Django 2.2.2 on 2020-02-17 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HackForms', '0002_auto_20200216_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='csv_file',
            field=models.FilePathField(path='C:\\Users\\kiran\\PycharmProjects\\HackFormsWeb\\media/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='data',
            field=models.FilePathField(path='C:\\Users\\kiran\\PycharmProjects\\HackFormsWeb\\media/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='empty_form',
            field=models.FilePathField(path='C:\\Users\\kiran\\PycharmProjects\\HackFormsWeb\\media/'),
        ),
        migrations.AlterField(
            model_name='project',
            name='zip_file',
            field=models.FilePathField(path='C:\\Users\\kiran\\PycharmProjects\\HackFormsWeb\\media/'),
        ),
    ]
