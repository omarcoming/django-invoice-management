from django.db import models


class Contact(models.Model):
    class Relation(models.TextChoices):
        CUSTOMER = 'CUSTOMER', 'Customer'
        DESIGNER = 'DESIGNER', 'Designer'
        CONTRACTOR = 'CONTRACTOR', 'Contractor'
        LEAD = 'LEAD', 'Lead'
        VENDOR = 'VENDOR', 'Vendor'
        FABRICATOR = 'FABRICATOR', 'Fabricator'
        OTHER = 'OTHER', 'Other'

    first_name = models.CharField('First Name', max_length=20, blank=True)
    last_name = models.CharField('Last Name', max_length=20, blank=True)
    phone = models.CharField('Phone Number', max_length=10, blank=True)
    alt_phone = models.CharField('Alt Phone Number', max_length=10, blank=True)
    company = models.CharField('Company', max_length=25, blank=True)
    email = models.EmailField('Email', null=True, blank=True)
    address = models.CharField('Address', max_length=25, blank=True)
    city = models.CharField('City', max_length=25, blank=True)
    state = models.CharField('State', max_length=2, blank=True)
    zip = models.CharField('Zip Code', max_length=5, blank=True)
    notes = models.TextField('Contact Notes', blank=True)
    relation = models.CharField('Relation', max_length=10, choices=Relation.choices, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Line(models.Model):
    class Material(models.TextChoices):
        NATURAL_QUARTZITE = 'NATURAL QUARTZITE', 'Natural Quartzite'
        ENGINEERED_QUARTZ = 'ENGINEERED QUARTZ', 'Engineered Quartz'
        GRANITE = 'GRANITE', 'Granite'
        MARBLE = 'MARBLE', 'Marble'
        DOLOMITE = 'DOLOMITE', 'Dolomite'
        SOAPSTONE = 'SOAPSTONE', 'Soapstone'
        OTHER = 'OTHER', 'Other'

    class Vendor(models.TextChoices):
        QARTS = 'Q-ARTS'
        MARBOLIS = 'MARBOLIS'
        SLABSTUDIO = 'SLABSTUDIO'
        WALKERZENGER = 'WALKERZENGER'
        OTHER = 'OTHER'

    class Finish(models.TextChoices):
        POLISHED = 'POLISHED'
        HONED = 'HONED'
        MATTE = 'MATTE'
        LEATHERED = 'LEATHERED'
        SATIN = 'SATIN'
        OTHER = 'OTHER'

    product = models.CharField('Product', max_length=25)
    material = models.CharField('Material', max_length=25, choices=Material.choices, blank=True)
    vendor = models.CharField('Vendor', max_length=25, blank=True)
    unit = models.CharField('Unit', default='ea', max_length=3)
    qty = models.IntegerField('Qty', default=0)
    price = models.DecimalField('Price', default=0, decimal_places=2, max_digits=9)
    prod_total = models.DecimalField('Line Total', default=0, decimal_places=2, max_digits=9)
    block = models.CharField('Block #', max_length=15, null=True, blank=True)
    length = models.DecimalField('Length', default=0, decimal_places=2, max_digits=5, null=True, blank=True)
    width = models.DecimalField('Width', default=0, decimal_places=2, max_digits=5, null=True, blank=True)
    payment = models.ForeignKey('Payment', on_delete=models.CASCADE, null=True, blank=True, related_name='lines')
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Line'
        verbose_name_plural = 'Lines'
        unique_together = ['date_created', 'payment']

class Payment(models.Model):
    class Status(models.TextChoices):
        BALANCE = 'BALANCE'
        PAID = 'PAID'
        CREDIT = 'CREDIT'

    class PaymentType(models.TextChoices):
        CASH = 'CASH'
        CHECK = 'CHECK'
        CARD = 'CARD'

    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    payment_type = models.CharField('Payment Method', max_length=20, blank=True, choices=PaymentType.choices)
    deposit = models.DecimalField('Deposit', decimal_places=2, max_digits=9, default=0)
    subtotal = models.DecimalField('Subtotal', decimal_places=2, max_digits=9, default=0)
    payment_status = models.CharField('Payment Status', max_length=10, blank=True, choices=Status.choices)
    balance = models.DecimalField('Balance', decimal_places=2, max_digits=9, default=0)
    tax = models.DecimalField('Sales Tax', decimal_places=2, max_digits=9, default=0)
    invoice_notes = models.TextField('Notes', blank=True)
    total = models.DecimalField('Total', decimal_places=2, max_digits=9, default=0)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, null=True, blank=True, related_name='payments')

    class Meta:
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'

    def __str__(self):
        return str(self.id)

    def calculate_tax(self, tax_rate=.0775):
        return self.subtotal * tax_rate


class Product(models.Model):
    class Material(models.TextChoices):
        NATURAL_QUARTZITE = 'NATURAL QUARTZITE', 'Natural Quartzite'
        ENGINEERED_QUARTZ = 'ENGINEERED QUARTZ', 'Engineered Quartz'
        GRANITE = 'GRANITE', 'Granite'
        MARBLE = 'MARBLE', 'Marble'
        DOLOMITE = 'DOLOMITE', 'Dolomite'
        SOAPSTONE = 'SOAPSTONE', 'Soapstone'
        OTHER = 'OTHER', 'Other'

    class Vendor(models.TextChoices):
        QARTS = 'Q-ARTS'
        MARBOLIS = 'MARBOLIS'
        SLABSTUDIO = 'SLABSTUDIO'

    class Finish(models.TextChoices):
        POLISHED = 'POLISHED'
        HONED = 'HONED'
        MATTE = 'MATTE'
        LEATHERED = 'LEATHERED'
        SATIN = 'SATIN'

    name = models.CharField('Product', max_length=255)
    vendor = models.CharField('Vendor', max_length=255, blank=True)
    material = models.CharField('Material', max_length=255, choices=Material.choices, blank=True)
    product_is_delete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    def __str__(self):
        return str(self.name)