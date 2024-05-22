# Generated by Django 5.0.2 on 2024-05-01 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0007_remove_car_height_remove_car_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='height',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='car',
            name='width',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=4, null=True),
        ),
    ]
