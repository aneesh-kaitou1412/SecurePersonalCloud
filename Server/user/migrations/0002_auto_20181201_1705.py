# Generated by Django 2.1.3 on 2018-12-01 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dirfile',
            old_name='md5code',
            new_name='b2code',
        ),
    ]
