# Generated by Django 5.0.6 on 2024-05-18 11:49

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
                ('name', models.CharField(max_length=100)),
                ('roll', models.IntegerField()),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
