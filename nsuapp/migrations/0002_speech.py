# Generated by Django 3.2.24 on 2024-07-18 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsuapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speech',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=3500)),
                ('name', models.CharField(max_length=350)),
            ],
        ),
    ]
