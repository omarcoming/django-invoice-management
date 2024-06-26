# Generated by Django 4.2.1 on 2024-05-22 21:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_remove_contractor_contractor_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_created', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=55, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=55, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=10, verbose_name='Phone Number')),
                ('alt_phone', models.CharField(blank=True, max_length=10, verbose_name='Alt Phone Number')),
                ('company', models.CharField(blank=True, max_length=55, verbose_name='Company')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=55, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=55, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=55, verbose_name='State')),
                ('zip', models.CharField(blank=True, max_length=9, verbose_name='Zip Code')),
                ('notes', models.TextField(blank=True, verbose_name='Customer Notes')),
                ('category', models.CharField(blank=True, choices=[('CONTRACTOR', 'Contractor'), ('DESIGNER', 'Designer'), ('CUSTOMER', 'Customer'), ('VENDOR', 'Vendor'), ('FABRICATOR', 'Fabricator'), ('LEAD', 'Lead'), ('OTHER', 'Other')], max_length=255, verbose_name='Category')),
            ],
        ),
        migrations.RemoveField(
            model_name='customer',
            name='customer_notes',
        ),
        migrations.AddField(
            model_name='customer',
            name='notes',
            field=models.TextField(blank=True, verbose_name='Customer Notes'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Balance'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='contractor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.contractor'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='invoice.customer'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='date_created',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
        migrations.AddField(
            model_name='invoice',
            name='deposit',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Deposit'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='invoice_notes',
            field=models.TextField(blank=True, verbose_name='Notes'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_status',
            field=models.CharField(blank=True, choices=[('BALANCE', 'Balance'), ('PAID', 'Paid'), ('CREDIT', 'Credit')], max_length=25, verbose_name='Payment Status'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='payment_type',
            field=models.CharField(blank=True, choices=[('CASH', 'Cash'), ('CHECK', 'Check'), ('CARD', 'Card')], max_length=25, verbose_name='Payment Method'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Subtotal'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='tax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Sales Tax'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9, verbose_name='Total'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='contractor_first_name',
            field=models.CharField(blank=True, max_length=55, verbose_name='Contractor First Name'),
        ),
        migrations.AlterField(
            model_name='contractor',
            name='contractor_last_name',
            field=models.CharField(blank=True, max_length=55, verbose_name='Contractor Last Name'),
        ),
        migrations.AlterField(
            model_name='productdetail',
            name='block',
            field=models.CharField(blank=True, max_length=55, null=True, verbose_name='Block No.'),
        ),
    ]
