# Generated by Django 4.1.2 on 2022-10-20 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_ems_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='ems_tehsil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortCode', models.CharField(default='', max_length=100)),
                ('isdeleted', models.BooleanField()),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.ems_district')),
            ],
        ),
    ]
