# Generated by Django 4.0.4 on 2022-07-22 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_desc_alter_product_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='outdesc',
            field=models.CharField(default=models.CharField(max_length=200), max_length=1000),
        ),
    ]