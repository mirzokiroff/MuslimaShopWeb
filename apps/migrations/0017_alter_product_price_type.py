# Generated by Django 5.1.2 on 2024-10-28 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0016_beautysalon_video_alter_beautysalon_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[("so'm", "SO'M"), ('$', 'USD')], max_length=4, verbose_name='Mahsulot Narxi Turi'),
        ),
    ]
