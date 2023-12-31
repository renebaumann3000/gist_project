# Generated by Django 4.2.6 on 2023-11-08 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profile/images/'),
        ),
        migrations.AddField(
            model_name='profile',
            name='socialmedia_url',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
