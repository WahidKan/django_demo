# Generated by Django 4.1.2 on 2022-10-24 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0008_ems_province_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='ems_district',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]