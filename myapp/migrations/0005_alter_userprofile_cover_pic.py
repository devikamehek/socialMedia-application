# Generated by Django 4.1.7 on 2023-04-21 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_userprofile_cover_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_pic',
            field=models.ImageField(blank=True, default='/profilepics/cover2.jpg', upload_to='coverpic'),
        ),
    ]
