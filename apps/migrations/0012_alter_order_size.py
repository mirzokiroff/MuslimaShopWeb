# Generated by Django 5.1.2 on 2024-10-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_order_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='size',
            field=models.CharField(max_length=149),
        ),
    ]
