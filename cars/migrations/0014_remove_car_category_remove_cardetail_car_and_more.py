# Generated by Django 5.0.2 on 2024-05-01 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0013_alter_cardetail_acceleration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='category',
        ),
        migrations.RemoveField(
            model_name='cardetail',
            name='car',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='CarDetail',
        ),
    ]
