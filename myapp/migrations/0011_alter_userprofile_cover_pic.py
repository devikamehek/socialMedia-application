# Generated by Django 4.1.7 on 2023-04-21 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_rename_cover_pic1_userprofile_cover_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='cover_pic',
            field=models.ImageField(blank=True, default='/profilepics/coverpic2.jpg', upload_to='coverpic'),
        ),
    ]
