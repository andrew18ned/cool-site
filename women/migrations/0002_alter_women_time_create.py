# Generated by Django 4.0.4 on 2022-05-03 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='time_create',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
