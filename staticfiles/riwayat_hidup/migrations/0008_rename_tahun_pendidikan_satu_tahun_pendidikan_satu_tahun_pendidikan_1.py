# Generated by Django 4.2.1 on 2023-05-28 07:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('riwayat_hidup', '0007_rename_tahun_pendidikan_1_tahun_pendidikan_satu_tahun_pendidikan_satu'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tahun_pendidikan_satu',
            old_name='tahun_pendidikan_satu',
            new_name='tahun_pendidikan_1',
        ),
    ]
