# Generated by Django 5.1.6 on 2025-03-10 15:01

import django.db.models.deletion
import items.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='barcode',
            field=models.CharField(default=items.models.generate_barcode, editable=False, max_length=13, unique=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='items.category'),
        ),
    ]
