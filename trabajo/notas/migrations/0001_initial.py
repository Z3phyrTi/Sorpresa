# Generated by Django 3.2.3 on 2021-06-04 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_limite', models.DateTimeField(auto_created=True, default=0, verbose_name='Fecha Limite')),
                ('titulo_nota', models.CharField(max_length=50, verbose_name='titulo nota')),
                ('descripcion_nota', models.CharField(default=0, max_length=200, verbose_name='descripcion nota')),
                ('fecha_creacion', models.DateTimeField(auto_now=True, verbose_name='Fecha de creacion')),
            ],
        ),
    ]
