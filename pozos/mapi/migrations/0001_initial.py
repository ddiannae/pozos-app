# Generated by Django 3.2.15 on 2022-11-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pozo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clave', models.CharField(max_length=64)),
                ('sitio', models.CharField(max_length=128)),
                ('organismo', models.CharField(max_length=128)),
                ('estado', models.CharField(max_length=128)),
                ('municipio', models.CharField(max_length=128)),
                ('acuifero', models.CharField(max_length=128)),
                ('subtipo', models.CharField(max_length=32)),
                ('lat', models.FloatField()),
                ('long', models.FloatField()),
                ('fe_total', models.FloatField()),
                ('fe_calidad', models.CharField(choices=[('excelente', 'Potable - Excelente'), ('sin_efectos', 'Sin efectos en la salud - Puede dar color al agua')], max_length=256)),
                ('semaforo', models.CharField(choices=[('verde', 'Verde'), ('amarillo', 'Amarillo'), ('rojo', 'Rojo')], max_length=32)),
            ],
        ),
    ]
