# Generated by Django 4.2.1 on 2023-05-28 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riwayat_hidup', '0010_tahun_pendidikan_dua'),
    ]

    operations = [
        migrations.CreateModel(
            name='tahun_pendidikan_empat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun_pendidikan_4', models.TextField(default='')),
                ('sekolah_pendidikan_4', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='tahun_pendidikan_tiga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun_pendidikan_3', models.TextField(default='')),
                ('sekolah_pendidikan_3', models.TextField(default='')),
            ],
        ),
    ]
