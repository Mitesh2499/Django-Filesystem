# Generated by Django 2.1.4 on 2019-03-21 11:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('FileApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UploadFile',
            new_name='files',
        ),
    ]