# Generated by Django 4.2.1 on 2024-05-31 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0018_payment_remove_line_invoice_line_date_created_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='line',
            options={'verbose_name': 'Line', 'verbose_name_plural': 'Lines'},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'Payment', 'verbose_name_plural': 'Payments'},
        ),
        migrations.AlterField(
            model_name='line',
            name='payment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lines', to='invoice.payment'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='payments', to='invoice.contact'),
        ),
        migrations.AlterUniqueTogether(
            name='line',
            unique_together={('date_created', 'payment')},
        ),
    ]
