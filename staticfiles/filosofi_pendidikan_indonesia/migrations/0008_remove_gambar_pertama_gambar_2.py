# Generated by Django 4.2.1 on 2023-05-29 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filosofi_pendidikan_indonesia', '0007_gambar_pertama_gambar_2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gambar_pertama',
            name='gambar_2',
        ),
    ]
