# Generated by Django 5.0.4 on 2024-04-12 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fake_product', '0010_remove_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
