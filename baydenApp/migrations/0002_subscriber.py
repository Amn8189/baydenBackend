# Generated by Django 5.0.1 on 2024-03-06 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baydenApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('secondname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
