# Generated by Django 5.0.1 on 2024-02-05 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration_form',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='registration_form',
            name='phone_no',
            field=models.CharField(max_length=50),
        ),
    ]
