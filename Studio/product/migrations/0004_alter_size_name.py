# Generated by Django 4.1.4 on 2023-02-14 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_size_size_product_variant_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.size'),
        ),
    ]
