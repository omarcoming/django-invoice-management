from datetime import datetime

from django import forms
from django.forms import formset_factory, modelformset_factory, inlineformset_factory
from django.forms.models import construct_instance, model_to_dict
from django.contrib.admin.widgets import AutocompleteSelect
from django.contrib import admin

from formset.collection import FormCollection
from formset.renderers.bootstrap import FormRenderer
from formset.utils import FormMixin
from formset.widgets import Selectize
from .models import *


class CustomerForm(forms.ModelForm):
    default_renderer = FormRenderer(
        form_css_classes='row',
        field_css_classes={
            '*': 'mb-1 col-4',
            'city': 'mb-1 col-3',
            'state': 'mb-1 col-1',
            'customer_notes': 'mb-1 col-12',
        }
    )

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
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone',
            }),
            'alt_phone': forms.TextInput(attrs={
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
            }),
            'zip': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'zip',
            }),
            'customer_notes': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'customer_notes',
                'placeholder': 'Enter customer notes',
                'rows': '2'
            }),
            'date_created': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'id': 'date_created',
                'value': datetime.now()
            })
        }


class ProductForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    # default_renderer = FormRenderer(
    #     form_css_classes='row',
    #     field_css_classes={
    #         'unit': 'mb-1 col-1',
    #         'prod_name': 'mb-1 col-3',
    #         '*': 'mb-1 col-2',
    #     }
    # )

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


class ProductDetailForm(forms.ModelForm):
    id = forms.IntegerField(required=False, widget=forms.HiddenInput)
    # default_renderer = FormRenderer(
    #     form_css_classes='row',
    #     field_css_classes={
    #         'product': 'mb-1 col-2',
    #         'qty': 'mb-1 col-1',
    #         'price': 'mb-1 col-2',
    #         'prod_total': 'mb-1 col-2',
    #         'block' : 'mb-1 col-2',
    #         'length': 'mb-1 col-1',
    #         'width': 'mb-1 col-1',
    #         # '*': 'mb-1 col-2',
    #     }
    # )

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
                'oninput': 'calculateProductTotal()'
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
    default_renderer = FormRenderer(
        collection_css_classes='container',
        form_css_classes='row',
        field_css_classes={
            'qty': 'mb-1 col-1',
            'unit'    : 'mb-1 col-1',
            'product': 'mb-1 col-2',
            'material': 'mb-1 col-2',
            # 'vendor'  : 'mb-1 col-2',
            'price'   : 'mb-1 col-1',
            'prod_total'   : 'mb-1 col-2',
            'block': 'mb-1 col-1',
            'length': 'mb-1 col-1',
            'width': 'mb-1 col-1',
            # '*': 'mb-1 col-2',
            },
    )

    extra_siblings = 0
    add_label = 'Add Product'

    product = ProductForm()
    product_detail = ProductDetailForm()

# class ProductCollection(FormCollection, FormMixin):
#     default_renderer = FormRenderer(
#         collection_css_classes='row',
#         field_css_classes={
#             'qty': 'mb-1 col-1',
#             'unit'    : 'mb-1 col-1',
#             'product': 'mb-1 col-2',
#             'material': 'mb-1 col-2',
#             # 'vendor'  : 'mb-1 col-2',
#             'price'   : 'mb-1 col-2',
#             'prod_total'   : 'mb-1 col-2',
#             '*': 'mb-1 col-2',
#             },
#     )
#
#     extra_siblings = 0
#     add_label = 'Add Product'
#
#     product = ProductForm()
#     product_detail = ProductDetailForm()