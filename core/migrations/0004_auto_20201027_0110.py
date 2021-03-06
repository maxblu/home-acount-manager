# Generated by Django 2.2.16 on 2020-10-27 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_action_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='action',
            name='amount',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='account',
            name='tipo',
            field=models.TextField(choices=[('CUC', 'CUC'), ('CUP', 'CUP'), ('USD', 'USD'), (None, 'Seleccione tipo de moneda')]),
        ),
        migrations.AlterField(
            model_name='action',
            name='act',
            field=models.TextField(choices=[('Ingreso', 'Ingresar'), ('Retiro', 'Retirar'), (None, 'Seleccione acción')]),
        ),
    ]
