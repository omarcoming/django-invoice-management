import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, ListView
from django.utils.encoding import force_str
from django.http.response import JsonResponse
from django.urls import reverse_lazy, reverse

from formset.views import EditCollectionView, FormCollectionView, FormView, FileUploadMixin, FormViewMixin, \
    IncompleteSelectResponseMixin

from .forms import *
from .models import *


class EditView(UpdateView, FormViewMixin):
    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
            if self.kwargs:
                return queryset.get(pk=self.kwargs['pk'])

    def get_success_url(self):
        model = self.model._meta.model_name
        if pk := self.object.id:
            return reverse(f'{model}-edit', kwargs={'pk': pk})
        else:
            return reverse(f'{model}-list')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.object:
            context_data['change'] = True
        else:
            context_data['add'] = True
        return context_data

    def form_valid(self, form):
        if extra_data := self.get_extra_data():
            if extra_data.get('add') is True:
                form.instance.save()
            if extra_data.get('delete') is True:
                form.instance.delete()
                response_data = {'success_url': force_str(self.get_success_url())}
                return JsonResponse(response_data)
        return super().form_valid(form)


class TotalsListView(ListView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['total_product'] = Totals.total_product
        # context['total_contact'] = Totals.total_contact
        # context['total_payment'] = Totals.total_payment
        # context['total_income'] = Totals.total_income
        return context


class ContactListView(TotalsListView):
    model = Contact
    template_name = 'invoice/contact-list.html'


class ContactEditView(EditView):
    model = Contact
    template_name = 'invoice/contact.html'
    form_class = ContactForm
    extra_context = None


class ContactCollectionView(EditCollectionView):
    model = Contact
    collection_class = ContactCollection
    template_name = 'invoice/contact-collection.html'


class LineListView(TotalsListView):
    model = Line
    template_name = 'invoice/line-list.html'


class LineEditView(EditView):
    model = Line
    template_name = 'invoice/line.html'
    form_class = LineForm
    extra_context = None


class LineCollectionView(EditCollectionView):
    model = Line
    collection_class = LineCollection
    template_name = 'invoice/line.html'


class PaymentListView(TotalsListView):
    model = Payment
    template_name = 'invoice/payment-list.html'


class PaymentEditView(EditView):
    model = Payment
    template_name = 'invoice/payment.html'
    form_class = PaymentForm
    extra_context = None


class PaymentCollectionView(EditCollectionView):
    model = Payment
    collection_class = PaymentCollection
    template_name = 'invoice/payment-collection.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
            if self.kwargs:
                return queryset.get(pk=self.kwargs['pk'])


# class InvoiceListView(TotalsListView):
#     model = Invoice
#     template_name =

class InvoiceEditView(EditView):
    model = Invoice
    template_name = 'invoice/invoice.html'
    form_class = InvoiceForm
    extra_context = None


# TODO: implement EditCollectionView?
class InvoiceCollectionView(EditCollectionView):
    model = Invoice
    collection_class = InvoiceCollection
    template_name = 'invoice/invoice-collection.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()
            if self.kwargs:
                return queryset.get(pk=self.kwargs['pk'])


class ProductListView(TotalsListView):
    model = Product
    template_name = 'invoice/product-list.html'


class ProductEditView(EditView, IncompleteSelectResponseMixin):
    model = Product
    template_name = 'invoice/product.html'
    form_class = ProductForm
    extra_context = None

    # def get_success_url(self):
    #     if pk := self.object.id:
    #         return reverse('product-edit', kwargs={'pk': pk})
    #     else:
    #         return reverse('product-list')

# class ProductCollectionView(EditCollectionView, IncompleteSelectResponseMixin):
#     collection_class = ProductCollection
#     template_name = 'invoice/product-collection.html'
#
#     # product = collection_class.declared_holders.get('product')
#     # product_detail = collection_class.declared_holders.get('product_detail')
#     success_url = 'success'
#     print('')
#
#     def get(self, request, *args, **kwargs):
#         """Handle GET requests: instantiate blank versions of the forms in the collection."""
#         return self.render_to_response(self.get_context_data())
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['form_collection'] = self.get_form_collection()
#         # context['product'] = self.product
#         # context['product_detail'] = self.product_detail
#         return context

# class Totals:
#     total_product = Product.objects.count()
#     total_contact = Contact.objects.count()
#     total_invoice = Invoice.objects.count()
#
#     @classmethod
#     def total_income(cls):
#         allInvoice = Invoice.objects.all()
#         totalIncome = 0
#         for curr in allInvoice:
#             totalIncome += curr.total
#         return totalIncome
