# Generated by Django 5.1.4 on 2025-01-03 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pegawai', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pegawai',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]