# Generated by Django 4.1.7 on 2023-02-26 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.IntegerField(max_length=10),
        ),
    ]
