# Generated by Django 4.1.7 on 2023-04-21 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_alter_userprofile_cover_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='cover_pic',
            new_name='cover_pics',
        ),
    ]
