from django.db import models


class Customer(models.Model):
    first_name = models.CharField('First Name', max_length=55, blank=True)
    last_name = models.CharField('Last Name', max_length=55, blank=True)
    phone = models.CharField('Phone Number', max_length=10, blank=True)
    alt_phone = models.CharField('Alt Phone Number', max_length=10, blank=True)
    company = models.CharField('Company', max_length=55, blank=True)
    email = models.EmailField('Email', null=True, blank=True)
    address = models.CharField('Address', max_length=55, blank=True)
    city = models.CharField('City', max_length=55, blank=True)
    state = models.CharField('State', max_length=55, blank=True)
    zip = models.CharField('Zip Code', max_length=9, blank=True)
    customer_notes = models.TextField(blank=True)

    date_created = models.DateTimeField(auto_created=True, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Contractor(models.Model):
    contractor_first_name = models.CharField('Contractor First Name', max_length=55, blank=True)
    contractor_last_name = models.CharField('Contractor Last Name', max_length=55, blank=True)
    contractor_company = models.CharField('Contractor Company', max_length=55, blank=True)
    contractor_phone = models.CharField('Contractor Phone', blank=True)
    contractor_email = models.EmailField('Contractor Email', null=True, blank=True)

    # contractor_address = models.CharField('Contractor Address', max_length=55, blank=True)
    # contractor_city = models.CharField('Contractor City', max_length=55, blank=True)
    # contractor_state = models.CharField('Contractor State', max_length=55, blank=True)
    # contractor_zip = models.CharField('Contractor Zip Code', max_length=9, blank=True)

    contractor_notes = models.TextField(blank=True)

    date_created = models.DateTimeField(auto_created=True, null=True, blank=True)


class Product(models.Model):
    prod_name = models.CharField('Product', max_length=255)
    unit = models.CharField('Unit', default='ea', max_length=255)
    vendor = models.CharField('Vendor', max_length=255, blank=True)
    product_is_delete = models.BooleanField(default=False)

    class Material(models.TextChoices):
        NATURAL_QUARTZITE = 'NATURAL QUARTZITE', 'Natural Quartzite'
        ENGINEERED_QUARTZ = 'ENGINEERED QUARTZ', 'Engineered Quartz'
        GRANITE = 'GRANITE', 'Granite'
        MARBLE = 'MARBLE', 'Marble'
        DOLOMITE = 'DOLOMITE', 'Dolomite'
        SOAPSTONE = 'SOAPSTONE', 'Soapstone'
        OTHER = 'OTHER', 'Other'

    material = models.CharField('Material', max_length=255, choices=Material.choices, blank=True)

    def __str__(self):
        return str(self.prod_name)


class ProductDetail(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    qty = models.DecimalField('Qty', default=0, decimal_places=2, max_digits=9)
    price = models.DecimalField('Price', default=0, decimal_places=2, max_digits=9)
    prod_total = models.DecimalField('Product Total', default=0, decimal_places=2, max_digits=9)

    block = models.CharField('Block #', max_length=55, null=True, blank=True)
    length = models.DecimalField('Length', default=0, decimal_places=2, max_digits=9, null=True, blank=True)
    width = models.DecimalField('Width', default=0, decimal_places=2, max_digits=9, null=True, blank=True)

    invoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, null=True, blank=True)


class Invoice(models.Model):
    class Status(models.TextChoices):
        BALANCE = 'BALANCE'
        PAID = 'PAID'
        CREDIT = 'CREDIT'

    class PaymentType(models.TextChoices):
        CASH = 'CASH'
        CHECK = 'CHECK'
        CARD = 'CARD'

    # invoice_date_created = models.DateTimeField(auto_now_add=True, default=datetime.datetime.now())
    date_created = models.DateTimeField(auto_created=True, null=True, blank=True)

    payment_type = models.CharField('Payment Method', max_length=25, blank=True, choices=PaymentType.choices)
    payment_status = models.CharField('Payment Status', max_length=25, blank=True, choices=Status.choices)
    subtotal = models.DecimalField('Subtotal', decimal_places=2, max_digits=9, default=0)
    tax = models.DecimalField('Sales Tax', decimal_places=2, max_digits=9, default=0)
    total = models.DecimalField('Total', decimal_places=2, max_digits=9, default=0)
    deposit = models.DecimalField('Deposit', decimal_places=2, max_digits=9, default=0)
    balance = models.DecimalField('Balance', decimal_places=2, max_digits=9, default=0)
    invoice_notes = models.TextField('Notes', blank=True)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return str(self.id)

    def calculate_tax(self, tax_rate=.0775):
        return self.subtotal * tax_rate