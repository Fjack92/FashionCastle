# Generated by Django 3.1 on 2021-08-25 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_userprofile_phone_numnber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
