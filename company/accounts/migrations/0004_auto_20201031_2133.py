# Generated by Django 3.0 on 2020-10-31 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20201031_1332'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='profile_pic',
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='image',
            field=models.ImageField(blank=True, default='images/None/no-img.jpg', null=True, upload_to='images'),
        ),
    ]
