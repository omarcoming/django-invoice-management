# Generated by Django 4.2.1 on 2024-05-23 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0009_alter_productdetail_invoice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetail',
            name='qty',
            field=models.IntegerField(default=0, verbose_name='Qty'),
        ),
    ]
