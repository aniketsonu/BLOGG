# Generated by Django 3.0.3 on 2020-03-16 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=20, unique=True, verbose_name='room_name')),
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
            ],
        ),
    ]
