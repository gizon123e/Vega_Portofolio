# Generated by Django 4.2.1 on 2023-05-29 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gambar_kedua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar_2', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='gambar_pertama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar_1', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='materi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materi', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='text_materi_kedua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_materi_2', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='text_materi_ketiga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_materi_3', models.TextField(blank=True, default='', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='text_materi_pertama',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_materi_1', models.TextField(blank=True, default='', null=True)),
            ],
        ),
    ]
