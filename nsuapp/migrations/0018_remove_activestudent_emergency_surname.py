# Generated by Django 3.2.24 on 2024-07-30 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nsuapp', '0017_alter_alumni_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activestudent',
            name='Emergency_Surname',
        ),
    ]
