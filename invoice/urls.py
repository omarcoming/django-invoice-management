from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', InvoiceCollectionView.as_view(extra_context={'add': True}), name='home'),

    # path('contactform', ContactListView.as_view(), name='contactform-list'),  # list view not handled here
    path('contactform/add/', ContactEditView.as_view(extra_context={'add': True}), name='contactform-add', ),
    path('contactform/<int:pk>/', ContactEditView.as_view(extra_context={'add': False}), name='contactform-edit', ),
    path('contacts', ContactListView.as_view(), name='contact-list'),  # list view not handled here
    path('contact/add/', ContactCollectionView.as_view(extra_context={'add': True}), name='contact-add', ),
    path('contact/<int:pk>/', ContactCollectionView.as_view(extra_context={'add': False}), name='contact-edit', ),


    # path('invoices', InvoiceCollectionListView.as_view(), name='invoice-list'),
    path('invoice/add/', InvoiceCollectionView.as_view(extra_context={'add': True}), name='invoice-add', ),
    path('invoice/<int:pk>/', InvoiceCollectionView.as_view(extra_context={'change': True}), name='invoice-edit', ),

    path('products', ProductListView.as_view(), name='product-list'),
    path('product/add/', ProductEditView.as_view(extra_context={'add': True}), name='product-add'),
    path('product/<int:pk>/', ProductEditView.as_view(extra_context={'add': False}), name='product-edit'),

    path('invoiceform/add/', InvoiceEditView.as_view(extra_context={'add': True}), name='invoiceform-add'),
    path('invoiceform/<int:pk>/', InvoiceEditView.as_view(extra_context={'add': False}), name='invoiceform-edit'),

    path('payments', PaymentListView.as_view(), name='payment-list'),  # list view not handled here
    path('payment/add/', PaymentCollectionView.as_view(extra_context={'add': True}), name='payment-add', ),
    path('payment/<int:pk>/', PaymentCollectionView.as_view(extra_context={'add': False}), name='payment-edit', ),

    path('lineforms', LineListView.as_view(), name='lineform-list'),
    path('lineform/add/', LineEditView.as_view(extra_context={'add': True}), name='lineform-add'),
    path('lineform/<int:pk>/', LineEditView.as_view(extra_context={'add': False}), name='lineform-edit'),

    path('line/add/', LineCollectionView.as_view(extra_context={'add': True}), name='line-add'),
    path('line/<int:pk>/', LineCollectionView.as_view(extra_context={'add': False}), name='line-edit'),

    # path('cc', ContactListView.as_view(), name='cc-list'),  # list view not handled here
    # path('cc/add/', ContactCollectionView.as_view(extra_context={'add': True}), name='cc-add', ),
    # path('cc/<int:pk>/', ContactCollectionView.as_view(extra_context={'add': False}), name='cc-edit', ),

]
