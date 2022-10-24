# Generated by Django 4.1.2 on 2022-10-20 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ems_country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortCode', models.CharField(default='', max_length=100)),
                ('isdeleted', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='ems_province',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shortCode', models.CharField(default='', max_length=100)),
                ('isdeleted', models.BooleanField()),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='info.ems_country')),
            ],
        ),
    ]