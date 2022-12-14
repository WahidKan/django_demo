# Generated by Django 4.1.2 on 2022-10-20 12:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0004_ems_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ems_constituency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('constituency_no', models.CharField(default='', max_length=100)),
                ('area_size', models.FloatField(default=0)),
                ('isdeleted', models.BooleanField()),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.ems_type')),
            ],
        ),
    ]
