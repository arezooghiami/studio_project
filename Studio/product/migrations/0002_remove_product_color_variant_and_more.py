# Generated by Django 4.1.4 on 2023-02-14 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='color_variant',
        ),
        migrations.RemoveField(
            model_name='product',
            name='size_variant',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(blank=True, null=True, related_name='color', to='product.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(blank=True, null=True, related_name='size', to='product.size', verbose_name='سایز'),
        ),
    ]
