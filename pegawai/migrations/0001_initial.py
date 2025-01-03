# Generated by Django 5.1.4 on 2024-12-28 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pegawai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=150)),
                ('nik', models.CharField(max_length=50, unique=True)),
                ('jabatan', models.CharField(max_length=50)),
            ],
        ),
    ]
