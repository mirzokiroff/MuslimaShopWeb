# Generated by Django 5.1.2 on 2024-10-22 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_product_size'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='sizes',
            field=models.ManyToManyField(blank=True, to='apps.size', verbose_name='Mahsulot Hajmlari'),
        ),
    ]
