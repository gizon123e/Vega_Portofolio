# Generated by Django 4.2.1 on 2023-05-29 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filosofi_pendidikan_indonesia', '0006_gambar_pertama'),
    ]

    operations = [
        migrations.AddField(
            model_name='gambar_pertama',
            name='gambar_2',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
