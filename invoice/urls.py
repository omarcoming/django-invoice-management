from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', CustomerListView.as_view(), name='home'),
    path('customers', CustomerListView.as_view(), name='customer-list'),  # list view not handled here
    path('customer/add/', CustomerEditView.as_view(extra_context={'add': True}), name='customer-add', ),
    path('customer/<int:pk>/', CustomerEditView.as_view(extra_context={'add': False}), name='customer-edit', ),

    path('contractors', ContractorListView.as_view(), name='contractor-list'),  # list view not handled here
    path('contractor/add/', ContractorEditView.as_view(extra_context={'add': True}), name='contractor-add', ),
    path('contractor/<int:pk>/', ContractorEditView.as_view(extra_context={'add': False}), name='contractor-edit', ),

    path('products', ProductListView.as_view(), name='product-list'),
    path('product/add/', ProductEditView.as_view(extra_context={'add': True}), name='product-add'),
    path('product/<int:pk>/', ProductEditView.as_view(extra_context={'add': False}), name='product-edit'),

    path('invoices', InvoiceListView.as_view(), name='invoice-list'),  # list view not handled here
    path('invoice/add/', InvoiceEditView.as_view(extra_context={'add': True}), name='invoice-add', ),
    path('invoice/<int:pk>/', InvoiceEditView.as_view(extra_context={'add': False}), name='invoice-edit', ),

    path('prodetails', ProductDetailListView.as_view(), name='prodetails-list'),
    path('prodetail/add/', ProductDetailEditView.as_view(extra_context={'add': True}), name='prodetail-add'),
    path('prodetail/<int:pk>/', ProductDetailEditView.as_view(extra_context={'add': False}), name='prodetail-edit'),

    path('product-collection/', ProductCollectionView.as_view(), name='product-collection'),
    path('invoice-collection/', InvoiceCollectionView.as_view(), name='invoice-collection'),

]
