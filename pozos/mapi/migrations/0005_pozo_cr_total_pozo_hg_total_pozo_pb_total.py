# Generated by Django 4.1.3 on 2023-01-02 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapi', '0004_pozo_as_total_pozo_cd_total_pozo_nno3_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pozo',
            name='cr_total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pozo',
            name='hg_total',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='pozo',
            name='pb_total',
            field=models.FloatField(null=True),
        ),
    ]
