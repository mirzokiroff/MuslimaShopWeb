# Generated by Django 5.1.2 on 2024-10-17 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About_Us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_address', models.CharField(blank=True, max_length=222, null=True, verbose_name="Do'kon Manzili")),
                ('work_time', models.CharField(blank=True, max_length=128, null=True, verbose_name="Do'kon Ishlash Vaqti")),
                ('phone', models.CharField(blank=True, max_length=128, null=True, verbose_name="Do'kon Raqami")),
                ('email', models.CharField(blank=True, max_length=128, null=True, verbose_name="Do'kon Pochtsi")),
                ('office_address', models.CharField(blank=True, max_length=222, null=True, verbose_name='Offis Manzili')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Kategoriya Nomi')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Kategoriya Haqida qisqacha')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Social_Media',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='social_media/', verbose_name='Ijtimoiy Tarmoq rasmi')),
                ('name', models.CharField(blank=True, max_length=128, null=True, verbose_name='Ijtimoiy Tarmoq nimi')),
                ('url', models.URLField(blank=True, null=True, verbose_name='Ijtimoiy Tarmoq url')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Mahsulot Nomi')),
                ('price', models.PositiveIntegerField(blank=True, null=True, verbose_name='Mahsulot Narxi')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Mahsulot Rasmi')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.category', verbose_name='Mahsulot Kategoriyasi')),
            ],
        ),
    ]
