# Generated by Django 4.1.4 on 2023-02-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_rename_uploaded_at_1_image_date_remove_image_image_3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('pdf_file', models.FileField(upload_to='pdf/')),
            ],
        ),
        migrations.RemoveField(
            model_name='registration1',
            name='id',
        ),
        migrations.AddField(
            model_name='registration1',
            name='email',
            field=models.EmailField(default=True, max_length=250, unique=True),
        ),
        migrations.AddField(
            model_name='registration1',
            name='phn_nmbr',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='registration1',
            name='village',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='registration1',
            name='dept_name',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='registration1',
            name='name',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='registration1',
            name='post_office',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='registration1',
            name='regi_no',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='registration1',
            name='session',
            field=models.CharField(default=True, max_length=250),
        ),
        migrations.AlterField(
            model_name='registration1',
            name='zilla',
            field=models.CharField(default=True, max_length=250),
        ),
    ]