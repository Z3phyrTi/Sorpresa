# Generated by Django 3.2.3 on 2021-06-04 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='nota',
            name='stock_producto',
            field=models.PositiveIntegerField(default=0, verbose_name='Stock del producto'),
        ),
    ]