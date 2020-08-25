from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView, TemplateView

from clients.forms.product import CategoryForm, CSVForm
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


class CategoryUploadView(SuccessMessageMixin, FormView):
    """Handle import csv file request."""

    form_class = CSVForm
    template_name = 'clients/category/upload_csv.html'

    def post(self, request, *args, **kwargs):
        csv_file = request.FILES["csv_file"]
        file_data = csv_file.read().decode("utf-8")
        lines = file_data.split("\n")
        lines.pop(0)

        for line in lines:
            fields = line.split(",")
            data_dict = {}
            if fields[0] not in ['', None]:
                data_dict["id"] = fields[0]
                data_dict["name"] = fields[1]
                data_dict["status"] = True if fields[2] == 'Active' else False

                if fields[3].strip("\r") not in ['Null', 'NULL']:
                    data_dict["parent_id_id"] = int(fields[3].strip("\r"))

                form = self.form_class(data_dict, request.FILES)
                if form.is_valid():
                    Category(**data_dict).save()
                else:
                    messages.error(request, form.errors.as_json())
                    return HttpResponseRedirect(reverse("clients:categoryUpload"))

        messages.success(request, "File uploaded.")
        return HttpResponseRedirect(reverse("clients:category"))

