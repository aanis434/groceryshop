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
        obj = categories()
        print('obj', obj)
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
    obj = Category.objects.filter(parent_id=None)
    print('obj', obj)
    i = 0
    data = []
    if obj:
        for item in obj:
            print('only_item: ', item)
            print('item id: ', item.id)
            if item.id:
                data[i]['sub'] = sub_categories(item.id)
                i = i + 1

        return data


def sub_categories(parent_id):
    obj = Category.objects.filter(parent_id=parent_id)
    i = 0
    data = []
    if obj:
        for item in obj:
            print(item)
            if item.id:
                data[i]['sub'] = sub_categories(item.id)
                i = i + 1

        return data
