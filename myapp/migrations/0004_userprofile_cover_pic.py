# Generated by Django 4.1.7 on 2023-04-21 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_userprofile_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cover_pic',
            field=models.ImageField(blank=True, default='/profilepics/cover1.jpg', upload_to='coverpic'),
        ),
    ]
