# Generated by Django 5.0.4 on 2024-05-17 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=250)),
                ('roll_number', models.IntegerField(max_length=100)),
                ('mobile_number', models.CharField(max_length=100)),
            ],
        ),
    ]
