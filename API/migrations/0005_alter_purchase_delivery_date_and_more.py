# Generated by Django 4.1.7 on 2023-11-28 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_alter_vendor_average_response_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='delivery_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Expected or actual delivery date of the order'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='issue_date',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Timestamp when the PO was issued to the vendor'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='quality_rating',
            field=models.FloatField(default=0.0, verbose_name='Rating given to the vendor for this PO'),
        ),
    ]