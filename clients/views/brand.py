import os

from django.conf import settings
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from clients.forms.product import BrandForm
from products.models import Brand


class BrandListView(ListView):
    model = Brand
    template_name = 'clients/brand/list.html'


class BrandCreateView(SuccessMessageMixin, CreateView):
    form_class = BrandForm
    model = Brand
    template_name = 'clients/brand/create.html'
    success_message = "%(name)s saved."


class BrandUpdateView(SuccessMessageMixin, UpdateView):
    form_class = BrandForm
    model = Brand
    template_name = 'clients/brand/update.html'
    success_message = "%(name)s updated."


class BrandDeleteView(SuccessMessageMixin, DeleteView):
    model = Brand
    success_url = reverse_lazy('clients:brand')
    success_message = "%(name)s was removed successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()

        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)
