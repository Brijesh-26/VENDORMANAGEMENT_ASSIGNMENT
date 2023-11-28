# Generated by Django 4.1.7 on 2023-11-28 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0008_remove_purchase_po_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='delivery_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 5, 19, 34, 16, 403157, tzinfo=datetime.timezone.utc), verbose_name='Expected or actual delivery date of the order'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='issue_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 28, 19, 34, 16, 403157, tzinfo=datetime.timezone.utc), verbose_name='Timestamp when the PO was issued to the vendor'),
        ),
    ]