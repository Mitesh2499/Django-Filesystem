# Generated by Django 2.1.4 on 2019-03-22 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FileApp', '0003_files_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='files',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='Files'),
        ),
    ]
