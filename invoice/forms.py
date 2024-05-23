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


# class ContactForm(Fieldset):
#     legend = 'Contact'
#
#     default_renderer = FormRenderer(
#         fieldset_css_classes='row',
#         field_css_classes={
#             '*': 'mb-1 col-4',
#             'city': 'mb-1 col-3',
#             'state': 'mb-1 col-1',
#             'contact_notes': 'mb-5 col-12',
#         }
#     )
#     first_name = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'first_name',
#                 'placeholder': 'Contact First Name',
#             })
#     )
#     last_name = forms.CharField(
#         required=False,
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'last_name',
#                 'placeholder': 'Contact Last Name',
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
#     contact_notes = forms.CharField(
#         required=False,
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'form-control',
#                 'id': 'contact_notes',
#                 'placeholder': 'Enter contact notes',
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


class ContactForm(ModelForm):
    default_renderer = FormRenderer(
        form_css_classes='row border p-1 m-1',
        field_css_classes={
            '*': 'mb-1 col-4',
            'city': 'mb-1 col-3',
            'state': 'mb-1 col-1',
            'contact_notes': 'mb-1 col-12',
            'extant': 'mb-5'
        },
    )
    legend = 'Contact'
    # hide_if = 'ext_contact.extant'

    class Meta:
        model = Contact
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
            'category',
            'notes',
        ]
        widgets = {
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
            'category': forms.Select(attrs={
                # 'class': 'form-control product-input mb-1 col-2',
                'class': 'form-control',
                'id': 'category',
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


# class ExtantContactForm(forms.Form):
#     extant = fields.BooleanField(
#         label='Existing Contact?',
#         required=False,
#     )
#     default_renderer = FormRenderer(
#         field_css_classes={
#             '*': 'mb-3'
#         },
#     )
#
# class ContactCollection(FormCollection):
#     contact = ContactForm()
#     ext_contact = ExtantContactForm()
#     legend = 'Contact'


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
            'name',
            'material',
            'vendor',
            'id',
        ]
        widgets = {
            'unit': forms.TextInput(attrs={
                # 'class': 'form-control product-input mb-1 col-1',
                'class': 'form-control',
                'id': 'unit',
            }),
            'name': Selectize(
                search_lookup='product_name__istartswith',
                attrs={
                    'data-minimum-input-length': 2,
                    'allowClear': 'true',
                    'data-placeholder': 'Find Product',
                    'dropdownAutoWidth': 'true',
                    'class': 'form-control product-input',
                }
            ),
            # 'name': forms.TextInput(attrs={
            #     # 'class': 'form-control product-input mb-1 col-3',
            #     'class': 'form-control',
            #     'id': 'prod_name',
            # }),
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
#     product = ProductForm()
#     related_field = 'productdetail'
#
#     def retrieve_instance(self, data):
#         if data := data.get('product'):
#             try:
#                 return self.instance.products.get(id=data.get('id') or 0)
#             except(AttributeError, Product.DoesNotExist, ValueError):
#                 return Product(name=data.get('name'), productdetail=)

class ProductDetailForm(ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    default_renderer = FormRenderer(
        form_css_classes='row',
        field_css_classes={
            'product': 'mb-1 col-2',
            'qty': 'mb-1 col-1',
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
            'block',
            'length',
            'width',
            'qty',
            'product',
            'price',
            'prod_total',
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

        # def model_to_dict(self, product):
        #     try:
        #         return model_to_dict(product.productdetail, fields=self._meta.fields, exclude=self._meta.exclude)
        #     except ProductDetail.DoesNotExist:
        #         return {}
        #
        # def construct_instance(self, product):
        #     try:
        #         productdetail = product.productdetail
        #     except ProductDetail.DoesNotExist:
        #         productdetail = ProductDetail(product=product)
        #     form = ProductDetailForm(data=self.cleaned_data, instance=productdetail)
        #     if form.is_valid():
        #         construct_instance(form, productdetail)
        #         form.save()

class ProductDetailCollection(FormCollection):
    min_siblings = 1
    productdetail = ProductDetailForm()
    add_label = 'Add Product'
    related_field = 'product'

    def retrieve_instance(self, data):
        if data := data.get('productdetail'):
            try:
                return self.instsance.productdetails.get(id=data.get('id') or 0)
            except(AttributeError, Product.DoesNotExist, ValueError):
                return ProductDetail(name=data.get('name'), product=self.instance)


class ProductCollection(FormCollection):
    extra_siblings = 0
    product = ProductForm()
    product_detail = ProductDetailCollection()


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
            'contact',
            'id',
        ]
        exclude = ['contact']
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
            'invoice_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'invoice_notes',
                'placeholder': 'Enter notes',
                'rows': '1'
            }),
        }


class InvoiceCollection(FormCollection):
    # contact = ContactCollection()
    contact = ContactForm()
    product = ProductCollection()
    invoice = InvoiceForm()
