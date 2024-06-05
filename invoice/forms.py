from datetime import datetime

from django.forms import fields, ModelForm
from django.forms.models import construct_instance, model_to_dict
from django import forms

from formset.collection import FormCollection
from formset.renderers.bootstrap import FormRenderer
from formset.fieldset import Fieldset, FieldsetMixin
from formset.utils import FormMixin
from formset.widgets import Selectize
from .models import *


class ContactForm(ModelForm):
    default_renderer = FormRenderer(
        form_css_classes='row border p-1 m-1',
        field_css_classes={
            '*': 'mb-1 col-4',
            'first_name': 'mb-1 col-3',
            'last_name': 'mb-1 col-3',
            'relation': 'mb-1 col-2',
            'company': 'mb-1 col-2',
            'phone': 'mb-1 col-2',
            'alt_phone': 'mb-1 col-2',
            'email': 'mb-1 col-2',
            'address': 'mb-1 col-2',
            'city': 'mb-1 col-3',
            'state': 'mb-1 col-1',
            'zip': 'mb-1 col-2',

            'notes': 'mb-1 col-12',
            'extant': 'mb-5'
        },
    )
    legend = 'Contact'

    # hide_if = 'ext_contact.extant'
    #
    class Meta:
        model = Contact
        fields = [
            'invoice',
            
            'first_name',
            'last_name',
            'relation',
            'company',
            'phone',
            'alt_phone',
            'email',
            'address',
            'city',
            'state',
            'zip',
            'notes',
        ]
        widgets = {
            'invoice': forms.HiddenInput(attrs={
                'class': 'form-control',
                'id': 'invoice',
            }),
                
            
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'first_name',
                'placeholder': 'Contact First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'last_name',
                'placeholder': 'Contact Last Name',
            }),
            'relation': forms.Select(attrs={
                # 'class': 'form-control product-input mb-1 col-2',
                'class': 'form-control',
                'id': 'relation',
            }),
            'phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'phone',
            }),
            'alt_phone': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'alt_phone',
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'company',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
            }),
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'address',
            }),
            'city': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'city',
            }),
            'state': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'state',
                'value': 'CA',
            }),
            'zip': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'zip',
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'contact_notes',
                'placeholder': 'Enter contact notes',
                'rows': '1'
            }),
            'date_created': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'id': 'date_created',
                'value': datetime.now()
            })
        }


class ContactCollection(FormCollection):
    min_siblings = 1
    contact = ContactForm()
    legend = 'SOLD TO:'
    add_label = 'Add Designer/Contractor'
    related_field = 'invoice'
    
    def retrieve_instance(self, data):
        if data := data.get('contact'):
            try:
                return self.instance.contacts.get(id=data.get('id') or 0)
            except(AttributeError, Contact.DoesNotExist, ValueError):
                return Contact(
                    invoice=self.instance,

                    first_name=data.get('first_name'),
                    last_name=data.get('last_name'),
                    relation=data.get('relation'),
                    company=data.get('company'),
                    phone=data.get('phone'),
                    alt_phone=data.get('alt_phone'),
                    email=data.get('email'),
                    address=data.get('address'),
                    city=data.get('city'),
                    state=data.get('state'),
                    zip=data.get('zip'),
                    notes=data.get('notes'),
                )


class LineForm(ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    default_renderer = FormRenderer(
        form_css_classes='row border p-1 m-1',
        field_css_classes={
            'unit': 'mb-1 col-1 mx-0',
            'qty': 'mb-1 col-1 mx-0',
            'product': 'mb-1 col-2 mx-0',
            'material': 'mb-1 col-1 mx-0',
            'vendor': 'mb-1 col-2 mx-0',
            'price': 'mb-1 col-1 mx-0',
            'prod_total': 'mb-1 col-1 mx-0',
            'block': 'mb-1 col-1 mx-0',
            'length': 'mb-1 col-1 mx-0',
            'width': 'mb-1 col-1 mx-0',
        }
    )

    class Meta:
        model = Line
        fields = [
            'payment',
            # 'date_created',
            'unit',
            'qty',
            'product',
            'material',
            'vendor',
            'block',
            'length',
            'width',
            'price',
            'prod_total',
            'id',
        ]
        widgets = {
            'payment': forms.HiddenInput(attrs={
                'class': 'form-control',
                'id': 'payment',
            }),
            'unit': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'unit',
            }),
            'qty': forms.NumberInput(attrs={
                'class': 'form-control product-input qty-product',
                'id': 'qty',
                'type': 'number',
                'oninput': 'calculateProductTotal()'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control product-input price-product',
                'id': 'product_price',
                'type': 'number',
                'oninput': 'calculateProductTotal()',
                'onblur': 'addDecimal()',
            }),
            'prod_total': forms.NumberInput(attrs={
                'class': 'form-control product-input total-product',
                'id': 'product_total',
                'type': 'number',
                'readonly': 'True',
            }),
            'block': forms.TextInput(attrs={
                'class': 'form-control product-input',
                'id': 'block',
            }),
            'length': forms.NumberInput(attrs={
                'class': 'form-control product-input',
                'id': 'length',
                'type': 'number',
            }),
            'width': forms.NumberInput(attrs={
                'class': 'form-control product-input',
                'id': 'width',
                'type': 'number',
            }),
            'product': forms.TextInput(attrs={
                # 'class': 'form-control product-input mb-1 col-3',
                'class': 'form-control',
                'id': 'product',
            }),
            'material': forms.Select(attrs={
                # 'class': 'form-control product-input mb-1 col-2',
                'class': 'form-control',
                'id': 'material',
            }),
            'vendor': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'vendor',
                'value': 'Q-ARTS',
            }),
        }

        # def model_to_dict(self, payment):
        #     try:
        #         return model_to_dict(payment.line, fields=self._meta.fields, exclude=self._metal.exclude)
        #     except Line.DoesNotExist:
        #         return {}
        #
        # def construct_instance(self, payment):
        #     try:
        #         line = payment.line
        #     except Line.DoesNotExist:
        #         line = Line(payment=payment)
        #     form = LineForm(data=self.cleaned_data, instance=line)
        #     if form.is_valid():
        #         construct_instance(form, line)
        #         form.save()


class LineCollection(FormCollection):
    min_siblings = 1
    line = LineForm()
    legend = 'LINE ITEMS:'
    add_label = 'Add line'
    related_field = 'payment'

    def retrieve_instance(self, data):
        if data := data.get('line'):
            try:
                return self.instance.lines.get(id=data.get('id') or 0)
            except(AttributeError, Line.DoesNotExist, ValueError):
                return Line(
                    payment=self.instance,
                    unit=data.get('unit'),
                    qty=data.get('qty'),
                    product=data.get('product'),
                    material=data.get('material'),
                    vendor=data.get('vendor'),
                    block=data.get('block'),
                    length=data.get('length'),
                    width=data.get('width'),
                    price=data.get('price'),
                    prod_total=data.get('prod_total'),
                )


class PaymentForm(ModelForm):
    default_renderer = FormRenderer(
        form_css_classes='row',
        field_css_classes={'*': 'mb-1 col-4',
                           'invoice_notes': 'mb-1 col-8'}
    )

    class Meta:
        model = Payment
        fields = [
            # 'invoice',
            'payment_type',
            'deposit',
            'subtotal',
            'payment_status',
            'balance',
            'tax',
            'notes',
            'total',

        ]
        # exclude = ['contact']
        widgets = {
            # 'invoice': forms.HiddenInput(attrs={
            #     'class': 'form-control',
            #     'id': 'invoice',
            # }),
            'payment_type': forms.Select(attrs={
                'class': 'form-control',
                'id': 'payment_type',
                'placeholder': 'Check',
            }),
            'payment_status': forms.Select(attrs={
                'class': 'form-control',
                'id': 'payment_status',
                'placeholder': 'PAID',
            }),
            'subtotal': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'subtotal',
                'placeholder': '0.00',
                'type': 'number',
                'readonly': 'True',
            }),
            'tax': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'tax',
                'type': 'number',
                'readonly': 'True'
            }),
            'total': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'total',
                'placeholder': '0.00',
                'type': 'number',
                'readonly': 'True',
            }),
            'deposit': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'deposit',
                'default': '0.00',
                'type': 'number',
                'oninput': 'calculateBalance()',
                'step': '0.01',
                'onblur': 'addDecimalToDeposit()',
            }),
            'balance': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'balance',
                'placeholder': '0.00',
                'type': 'number',
                'readonly': 'True'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'invoice_notes',
                'placeholder': 'Enter notes',
                'rows': '1'
            }),
        }

        # def is_valid(self):
        #     valid = super().is_valid()
        #     return valid

        # def model_to_dict(self, invoice):
        #     try:
        #         return model_to_dict(invoice.payment, fields=self._meta.fields, exclude=self._meta.exclude)
        #     except Payment.DoesNotExist:
        #         return {}
        #
        # def construct_instance(self, invoice):
        #     try:
        #         payment = invoice.payment
        #     except Payment.DoesNotExist:
        #         payment = Payment(invoice=invoice)
        #     form = PaymentForm(data=self.cleaned_data, instance=payment)
        #     if form.is_valid():
        #         construct_instance(form, payment)
        #         form.save()


class PaymentCollection(FormCollection):
    lines = LineCollection()
    payment = PaymentForm()

    def retrieve_instance(self, data):
        if data := self.data.get('payment'):
            return Payment(
                # invoice=self.instance,
                payment_type=data.get('payment_type'),
                deposit=data.get('deposit'),
                subtotal=data.get('subtotal'),
                payment_status=data.get('payment_status'),
                balance=data.get('balance'),
                tax=data.get('tax'),
                notes=data.get('notes'),
                total=data.get('total'),
            )


class InvoiceForm(ModelForm):
    default_renderer = FormRenderer(
        form_css_classes='row',
        field_css_classes={'*': 'mb-1 col-4', }
    )

    class Meta:
        model = Invoice
        fields = [
            'notes',
        ]

        widgets = {
            # 'payment': forms.HiddenInput(attrs={
            #     'class': 'form-control',
            #     'id': 'payment',
            # }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'notes',
            }),
        }

        def model_to_dict(self, payment):
            try:
                return model_to_dict(payment.invoice, fields=self._meta.fields, exclude=self._meta.exclude)
            except Invoice.DoesNotExist:
                return {}

        def construct_instance(self, payment):
            try:
                invoice = payment.invoice
            except Invoice.DoesNotExist:
                invoice = Invoice(payment=payment)
            form = InvoiceForm(data=self.cleaned_data, instance=invoice)
            if form.is_valid():
                construct_instance(form, invoice)
                form.save()


class InvoiceCollection(FormCollection):
    invoice = InvoiceForm()
    contact = ContactCollection()
    payment = PaymentCollection()


class ProductForm(ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    default_renderer = FormRenderer(
        form_css_classes='row',
        field_css_classes={
            'unit': 'm-1 col-1',
            'prod_name': 'm-1 col-3',
            '*': 'm-1 col-2',
        }
    )

    class Meta:
        model = Product
        fields = [
            'name',
            'material',
            'vendor',
            'id',
        ]
        widgets = {
            # 'name': Selectize(
            #     search_lookup='product_name__istartswith',
            #     attrs={
            #         'data-minimum-input-length': 2,
            #         'allowClear': 'true',
            #         'data-placeholder': 'Find Product',
            #         'dropdownAutoWidth': 'true',
            #         'class': 'form-control product-input',
            #     }
            # ),
            'name': forms.TextInput(attrs={
                # 'class': 'form-control product-input mb-1 col-3',
                'class': 'form-control',
                'id': 'prod_name',
            }),
            'material': forms.Select(attrs={
                # 'class': 'form-control product-input mb-1 col-2',
                'class': 'form-control',
                'id': 'material',
            }),
            'vendor': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'vendor',
                'value': 'Q-ARTS',
            }),
        }

# class ProductCollection(FormCollection):
#     extra_siblings = 0
#     product = ProductForm()
#     product_detail = LineCollection()
