# Generated by Django 4.1.2 on 2022-10-24 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0007_remove_ems_constituency_isdeleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='ems_province',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
