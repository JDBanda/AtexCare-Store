# Generated by Django 3.1.7 on 2021-03-30 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0005_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(null=True),
        ),
    ]
