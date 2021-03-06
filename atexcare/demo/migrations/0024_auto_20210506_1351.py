# Generated by Django 3.2 on 2021-05-06 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0023_alter_compra_status_compra'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carrito',
            name='status',
            field=models.IntegerField(choices=[(0, 'Pagado'), (1, 'Activo'), (2, 'En proceso'), (3, 'Entregado')], default=1),
        ),
        migrations.AlterField(
            model_name='compra',
            name='status_compra',
            field=models.IntegerField(choices=[(0, 'Pagado'), (1, 'Activo'), (2, 'En proceso'), (3, 'Entregado')], default=2),
        ),
    ]
