# Generated by Django 4.2.2 on 2023-10-09 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exhibition',
            name='tickets_quantity',
            field=models.PositiveIntegerField(default=0),
        ),
    ]