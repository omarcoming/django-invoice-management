# Generated by Django 4.2.1 on 2024-05-23 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_contact_remove_customer_customer_notes_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='category',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='contractor',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='customer',
        ),
        migrations.AddField(
            model_name='invoice',
            name='contact',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.contact'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Contact Notes'),
        ),
        migrations.DeleteModel(
            name='Contractor',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]
