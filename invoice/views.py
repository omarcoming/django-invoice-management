import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView
from django.utils.encoding import force_str
from django.http.response import JsonResponse
from django.urls import reverse_lazy, reverse

from formset.views import EditCollectionView, FormCollectionView, FormView, FileUploadMixin, FormViewMixin

from .forms import *
from .models import *


# class Totals:
#     total_product = Product.objects.count()
#     total_customer = Customer.objects.count()
#     total_invoice = Invoice.objects.count()
#
#     @classmethod
#     def total_income(cls):
#         allInvoice = Invoice.objects.all()
#         totalIncome = 0
#         for curr in allInvoice:
#             totalIncome += curr.total
#         return totalIncome

class EditView(FormView, UpdateView):
    def get_object(self, queryset=None):
        if self.extra_context['add'] is False:
            return super().get_object(queryset)

    def form_valid(self, form):
        if extra_data := self.get_extra_data():
            if extra_data.get('delete') is True:
                self.object.delete()
                success_url = self.get_success_url()
                response_data = {'success_url': force_str(success_url)} if success_url else {}
                return JsonResponse(response_data)
        return super().form_valid(form)


class TotalsListView(ListView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['total_product'] = Totals.total_product
        # context['total_customer'] = Totals.total_customer
        # context['total_invoice'] = Totals.total_invoice
        # context['total_income'] = Totals.total_income
        return context


class CustomerListView(TotalsListView):
    model = Customer
    template_name = 'invoice/customer-list.html'


class CustomerEditView(EditView):
    model = Customer
    template_name = 'invoice/customer_add.html'
    form_class = CustomerForm
    extra_context = None

    def get_success_url(self):
        if pk := self.object.id:
            return reverse('customer-edit', kwargs={'pk': pk})
        else:
            return reverse('customer-list')


class ProductListView(TotalsListView):
    model = Product
    template_name = 'invoice/product-list.html'


class ProductEditView(EditView):
    model = Product
    template_name = 'invoice/product-add.html'
    form_class = ProductForm
    extra_context = None

    def get_success_url(self):
        if pk := self.object.id:
            return reverse('product-edit', kwargs={'pk': pk})
        else:
            return reverse('product-list')


class ProductDetailListView(TotalsListView):
    model = ProductDetail
    template_name = 'invoice/prodetail-list.html'


class ProductDetailEditView(FormView, UpdateView):
    model = ProductDetail
    template_name = 'invoice/prodetail-add.html'
    form_class = ProductDetailForm
    extra_context = None

    def get_success_url(self):
        if pk := self.object.id:
            return reverse('prodetail-edit', kwargs={'pk': pk})
        else:
            return reverse('prodetails-list')


class ProductCollectionView(FormCollectionView):
    collection_class = ProductCollection
    template_name = 'invoice/product-collection.html'

    product = collection_class.declared_holders.get('product')
    product_detail = collection_class.declared_holders.get('product_detail')
    success_url = 'success'
    print('')

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate blank versions of the forms in the collection."""
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_collection'] = self.get_form_collection()
        # context['product'] = self.product
        # context['product_detail'] = self.product_detail
        return context


class ContractorListView(TotalsListView):
    model = Contractor
    template_name = 'invoice/contractor-list.html'


class ContractorEditView(EditView):
    model = Contractor
    template_name = 'invoice/contractor-add.html'
    form_class = ContractorForm
    extra_context = None

    def get_success_url(self):
        if pk := self.object.id:
            return reverse('contractor-edit', kwargs={'pk': pk})
        else:
            return reverse('contractor-list')


class InvoiceListView(TotalsListView):
    model = Invoice
    template_name = 'invoice/invoice-list.html'


class InvoiceEditView(EditView):
    model = Invoice
    template_name = 'invoice/invoice-add.html'
    form_class = InvoiceForm
    extra_context = None

    def get_success_url(self):
        if pk := self.object.id:
            return reverse('invoice-edit', kwargs={'pk': pk})
        else:
            return reverse('invoice-list')


class InvoiceCollectionView(FormCollectionView):
    collection_class = InvoiceCollection
    template_name = 'invoice/invoice-collection.html'

    customer = CustomerForm()
    contractor = ContractorForm()
    product = ProductCollection()
    invoice = InvoiceForm()

    def get(self, request, *args, **kwargs):
        """Handle GET requests: instantiate blank versions of the forms in the collection."""
        return self.render_to_response(self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_collection'] = self.get_form_collection()
        context['customer'] = self.customer
        context['contractor'] = self.contractor
        context['product'] = self.product
        context['invoice'] = self.invoice
        return context