# Generated by Django 3.2.3 on 2021-06-04 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0003_remove_nota_stock_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='fecha_limite',
            field=models.DurationField(verbose_name='Fecha Limite'),
        ),
    ]