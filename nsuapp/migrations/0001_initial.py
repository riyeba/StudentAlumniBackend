# Generated by Django 3.2.24 on 2024-07-14 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveStudent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=150)),
                ('First_name', models.CharField(max_length=150)),
                ('Degree', models.CharField(max_length=150)),
                ('College', models.CharField(max_length=150)),
                ('Phone_number', models.CharField(max_length=150)),
                ('Address', models.CharField(max_length=250)),
                ('FamilyinSaudi', models.CharField(blank=True, max_length=30)),
                ('Building_number', models.IntegerField()),
                ('Room_number', models.IntegerField()),
                ('Emergency_Surname', models.CharField(blank=True, max_length=150)),
                ('Emergency_FirstName', models.CharField(blank=True, max_length=150)),
                ('Relationship', models.CharField(blank=True, max_length=150)),
                ('Nextofkin_mobile', models.CharField(max_length=150)),
                ('Nextofkin_city', models.CharField(blank=True, max_length=150)),
                ('photo', models.ImageField(upload_to='image/')),
                ('auth_email', models.CharField(max_length=100, unique=True)),
                ('auth_password', models.CharField(max_length=30)),
                ('verify_token', models.CharField(max_length=16, null=True)),
                ('email_sent_condition_met', models.BooleanField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Surname', models.CharField(max_length=150)),
                ('First_name', models.CharField(max_length=150)),
                ('Graduation_year', models.CharField(max_length=150)),
                ('Degree', models.CharField(max_length=150)),
                ('College', models.CharField(max_length=150)),
                ('Residence_Country', models.CharField(max_length=150)),
                ('Occupation', models.CharField(blank=True, max_length=150)),
                ('photo', models.ImageField(upload_to='image/')),
                ('Phone_number', models.CharField(max_length=150)),
                ('auth_email', models.CharField(max_length=150, unique=True)),
                ('auth_password', models.CharField(max_length=150)),
                ('verify_token', models.CharField(max_length=16, null=True)),
                ('email_sent_condition_met', models.BooleanField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=150)),
                ('title', models.CharField(blank=True, max_length=150)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur_name', models.CharField(blank=True, max_length=30)),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
