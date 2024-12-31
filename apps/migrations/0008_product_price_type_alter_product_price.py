# Generated by Django 5.1.2 on 2024-10-22 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0007_size_remove_product_size_product_sizes'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_type',
            field=models.CharField(choices=[('uzs', 'UZS'), ('usd', 'USD')], default='uzs', max_length=3, verbose_name='Mahsulot Narxi Turi'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveIntegerField(default=0, verbose_name='Mahsulot Narxi'),
        ),
    ]
