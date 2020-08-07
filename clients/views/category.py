from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from clients.forms.product import CategoryForm
from products.models import Category
from django.db.models import Q


class CategoryListView(ListView):
    model = Category
    template_name = 'clients/category/list.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Category.objects.filter(
            parent_id=None)
        return context


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
