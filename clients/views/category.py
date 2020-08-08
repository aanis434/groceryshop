from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from clients.forms.product import CategoryForm
from products.models import Category


class CategoryListView(ListView):
    model = Category
    template_name = 'clients/category/list.html'


class CategoryCreateView(SuccessMessageMixin, CreateView):
    form_class = CategoryForm
    model = Category
    template_name = 'clients/category/create.html'
    success_message = "%(name)s saved."


class CategoryUpdateView(SuccessMessageMixin, UpdateView):
    form_class = CategoryForm
    model = Category
    template_name = 'clients/category/update.html'
    success_message = "%(name)s updated."


class CategoryDeleteView(SuccessMessageMixin, DeleteView):
    model = Category
    success_url = reverse_lazy('clients:category')
    success_message = "%(name)s was removed successfully"

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super().delete(request, *args, **kwargs)
