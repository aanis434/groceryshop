from django.views.generic import TemplateView

from helpers import generate_category
from products.models import Category


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header_categories'] = generate_category()
        context['categories'] = Category.objects.all()
        return context
