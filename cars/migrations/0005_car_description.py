# Generated by Django 4.2.20 on 2025-04-30 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_carinventory_alter_car_plate'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
