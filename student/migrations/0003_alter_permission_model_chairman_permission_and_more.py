# Generated by Django 4.1.4 on 2023-02-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_permission_model_pdf_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission_model',
            name='chairman_permission',
            field=models.CharField(default='wa', max_length=10),
        ),
        migrations.AlterField(
            model_name='permission_model',
            name='examcontroller_permission',
            field=models.CharField(default='wa', max_length=10),
        ),
        migrations.AlterField(
            model_name='permission_model',
            name='hallprovost_permission',
            field=models.CharField(default='wa', max_length=10),
        ),
    ]
