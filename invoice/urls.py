from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', InvoiceCollectionView.as_view(), name='home'),

    path('contacts', ContactListView.as_view(), name='contact-list'),  # list view not handled here
    path('contact/add/', ContactEditView.as_view(extra_context={'add': True}), name='contact-add', ),
    path('contact/<int:pk>/', ContactEditView.as_view(extra_context={'add': False}), name='contact-edit', ),

    path('invoices', InvoiceListView.as_view(), name='invoice-list'),  # list view not handled here
    path('invoice/add/', InvoiceCollectionView.as_view(extra_context={'add': True}), name='invoice-add', ),
    path('invoice/<int:pk>/', InvoiceCollectionView.as_view(extra_context={'add': False}), name='invoice-edit', ),

    # path('cc', ContactListView.as_view(), name='cc-list'),  # list view not handled here
    # path('cc/add/', ContactCollectionView.as_view(extra_context={'add': True}), name='cc-add', ),
    # path('cc/<int:pk>/', ContactCollectionView.as_view(extra_context={'add': False}), name='cc-edit', ),

    path('products', ProductListView.as_view(), name='product-list'),
    path('product/add/', ProductEditView.as_view(extra_context={'add': True}), name='product-add'),
    path('product/<int:pk>/', ProductEditView.as_view(extra_context={'add': False}), name='product-edit'),

    # path('invoices', InvoiceListView.as_view(), name='invoice-list'),  # list view not handled here
    # path('invoice/add/', InvoiceEditView.as_view(extra_context={'add': True}), name='invoice-add', ),
    # path('invoice/<int:pk>/', InvoiceEditView.as_view(extra_context={'add': False}), name='invoice-edit', ),

    path('prodetails', ProductDetailListView.as_view(), name='productdetails-list'),
    path('prodetail/add/', ProductDetailEditView.as_view(extra_context={'add': True}), name='productdetails-add'),
    path('prodetail/<int:pk>/', ProductDetailEditView.as_view(extra_context={'add': False}), name='productdetails-edit'),

    path('product-collection/', ProductCollectionView.as_view(), name='product-collection'),
    path('invoice-collection/', InvoiceCollectionView.as_view(), name='invoice-collection'),

]
