from datetime import datetime

from django.forms import fields, ModelForm
from django import forms
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.forms.models import construct_instance, model_to_dict
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

from formset.collection import FormCollection
from formset.renderers.bootstrap import FormRenderer
from formset.fieldset import Fieldset, FieldsetMixin
from formset.utils import FormMixin
from formset.widgets import Selectize
from .models import *


# class CustomerForm(Fieldset):
#     legend = 'Customer'
#
#     default_renderer = FormRenderer(
#         fieldset_css_classes='row',
#         field_css_classes={
#             '*': 'mb-1 col-4',
#             'city': 'mb-1 col-3',
#             'state': 'mb-1 col-1',
#             'customer_notes': 'mb-5 col-12',
#         }
#     )
#     first_name = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'first_name',
#                 'placeholder': 'Customer First Name',
#             })
#     )
#     last_name = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'last_name',
#                 'placeholder': 'Customer Last Name',
#             })
#     )
#     phone = forms.CharField(
#         required=False,
#         widget=forms.NumberInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'phone',
#             })
#     )
#     alt_phone = forms.CharField(
#         required=False,
#         widget=forms.NumberInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'phone',
#             })
#     )
#
#     company = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'company',
#             })
#     )
#
#     email = forms.EmailField(
#         required=False,
#         widget=forms.EmailInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'email',
#             })
#     )
#
#     address = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'address',
#             })
#     )
#
#     city = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'city',
#             })
#     )
#
#     state = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'state',
#                 'value': 'CA',
#             })
#     )
#
#     zip = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'zip',
#             })
#     )
#
#     customer_notes = forms.CharField(
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'customer_notes',
#                 'placeholder': 'Enter customer notes',
#                 'rows': '1'
#             })
#     )
#
#     date_created = forms.CharField(
#         required=False,
#         widget=forms.DateTimeInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'date_created',
#                 'value': datetime.now(),
#                 'hidden': True,
#             }),
#         label=False,
#     )


class CustomerForm(ModelForm):
    default_renderer = FormRenderer(
        form_css_classes='row border p-1 m-1',
        field_css_classes={
            '*': 'mb-1 col-4',
            'city': 'mb-1 col-3',
            'state': 'mb-1 col-1',
            'customer_notes': 'mb-1 col-12',
            'extant': 'mb-5'
        },
    )
    legend = 'Customer'
    hide_if = 'ext_customer.extant'

    class Meta:
        model = Customer
        fields = [
            'first_name',
            'last_name',
            'company',
            'phone',
            'alt_phone',
            'email',
            'address',
            'city',
            'state',
            'zip',
            'customer_notes',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'first_name',
                'placeholder': 'Customer First Name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'last_name',
                'placeholder': 'Customer Last Name',
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
            'customer_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'customer_notes',
                'placeholder': 'Enter customer notes',
                'rows': '1'
            }),
            'date_created': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'id': 'date_created',
                'value': datetime.now()
            })
        }


class ExtantCustomerForm(forms.Form):
    extant = fields.BooleanField(
        label='Existing Customer?',
        required=False,
    )
    default_renderer = FormRenderer(
        field_css_classes={
            '*': 'mb-3'
        },
    )


class CustomerCollection(FormCollection):
    customer = CustomerForm()
    ext_customer = ExtantCustomerForm()
    legend = 'Customer'



class ContractorForm(ModelForm):
    default_renderer = FormRenderer(
        form_css_classes='row border p-1 m-1',
        field_css_classes={
            '*': 'mb-1 col-3',
            'contractor_notes': 'mb-1 col-9',
        }
    )
    legend = 'Contractor'
    hide_if = 'ext_contractor.extant'

    class Meta:
        model = Contractor
        fields = [
            'contractor_first_name',
            'contractor_last_name',
            'contractor_phone',
            'contractor_email',
            'contractor_company',
            'contractor_notes',
        ]
        widgets = {
            'contractor_first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contractor_first_name',
                'placeholder': 'First Name',
            }),
            'contractor_last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contractor_last_name',
                'placeholder': 'Last Name',
            }),
            'contractor_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contractor_phone',
            }),
            # 'alt_phone': forms.TextInput(attrs={
            #     'class': 'form-control',
            #     'id': 'alt_phone',
            # }),
            'contractor_company': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'contractor_company',
            }),
            'contractor_email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'contractor_email',
            }),
            'contractor_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'contractor_notes',
                'placeholder': 'Enter contractor notes',
                'rows': '1'
            }),
            'date_created': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'id': 'date_created',
                'value': datetime.now()
            })
        }


class ExtantContractorForm(forms.Form):
    extant = fields.BooleanField(
        label='Working with contractor?',
        required=False,
    )
    default_renderer = FormRenderer(
        field_css_classes={
            '*': 'mb-3'
        },
    )


class ContractorCollection(FormCollection):
    contractor = ContractorForm()
    ext_contractor = ExtantContractorForm()
    legend = 'Contractor'


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
            'unit',
            'prod_name',
            'material',
            # 'vendor',
            'id',
        ]
        widgets = {
            'unit': forms.TextInput(attrs={
                # 'class': 'form-control product-input mb-1 col-1',
                'class': 'form-control',
                'id': 'unit',
            }),
            'prod_name': forms.TextInput(attrs={
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
                'hidden': 'true',
                'value': 'Q-ARTS',
            }),
        }


class ProductDetailForm(ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    default_renderer = FormRenderer(
        form_css_classes='row',
        field_css_classes={
            'product': 'mb-1 col-2',
            'qty': 'mb-1 col-2',
            'price': 'mb-1 col-2',
            'prod_total': 'mb-1 col-2',
            'block': 'mb-1 col-2',
            'length': 'mb-1 col-1',
            'width': 'mb-1 col-1',
            # '*': 'm-1 col-2',
        }
    )

    class Meta:
        model = ProductDetail
        fields = [
            'product',
            'qty',
            'price',
            'prod_total',
            'block',
            'length',
            'width',
            'id',
        ]
        widgets = {
            'product': Selectize(
                search_lookup='product_name__istartswith',
                attrs={
                    'data-minimum-input-length': 2,
                    'allowClear': 'true',
                    'data-placeholder': 'Find Product',
                    'dropdownAutoWidth': 'true',
                    'class': 'form-control product-input',
                }
            ),
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
            })
        }


class ProductCollection(FormCollection):
    extra_siblings = 0
    add_label = 'Add Product'
    # product = ProductForm()
    product_detail = ProductDetailForm()


class InvoiceForm(ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    default_renderer = FormRenderer(
        form_css_classes='row',
        field_css_classes={'*': 'mb-1 col-4',
                           'invoice_notes': 'mb-1 col-8'}
    )

    class Meta:
        model = Invoice
        fields = [
            'payment_type',
            'deposit',
            'subtotal',
            'payment_status',
            'balance',
            'tax',
            'invoice_notes',
            'total',
            'customer',
            'id',
        ]
        exclude = ['customer']
        widgets = {
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
                'step': '0.00',
                'onblur': 'addDecimalToDeposit()',
            }),
            'balance': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'balance',
                'placeholder': '0.00',
                'type': 'number',
                'readonly': 'True'
            }),
            'invoice_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'invoice_notes',
                'placeholder': 'Enter notes',
                'rows': '1'
            }),
        }


class InvoiceCollection(FormCollection):
    customer = CustomerCollection()
    contractor = ContractorCollection()
    product = ProductCollection()
    invoice = InvoiceForm()
