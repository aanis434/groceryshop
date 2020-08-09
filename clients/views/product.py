from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from clients.forms.product import ProductForm
from products.models import Product, Category


class ProductListView(ListView):
    model = Product
    template_name = 'clients/product/list.html'


class ProductCreateView(SuccessMessageMixin, CreateView):
    form_class = ProductForm
    model = Product
    template_name = 'clients/product/create.html'
    success_message = "%(name)s saved."

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categories()
        self.categories()
        return context

    def categories(self):
        print('self fun')


class ProductUpdateView(SuccessMessageMixin, UpdateView):
    form_class = ProductForm
    model = Product
    template_name = 'clients/product/update.html'
    success_message = "%(name)s updated."


class ProductDeleteView(SuccessMessageMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('clients:product')
    success_message = "%(name)s was removed successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)


def categories():
    pass


