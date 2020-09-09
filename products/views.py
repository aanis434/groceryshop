from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView

from helpers import generate_category
from products.models import Category


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'
        context['header_categories'] = generate_category()
        context['explore_categories'] = Category.objects.filter(parent_id=None, status=True)

        return context


class FilterByCategoryView(ListView):
    template_name = 'products/filter_by_category.html'
    model = Category

    def category(self):
        categories = ''
        parent_category = Category.objects.filter(parent_id=None, status=True)

        for parent in parent_category:
            categories += "<div class=\"single_filter_card\">"
            if parent.parent_category.count() > 0:
                categories += "<h5>"
                categories += "<a href=\"/{}/\" role=\"button\" class=\"collapsed\">{}</a>".format(parent.slug, parent.name)
                categories += "<a href=\"#category_{}\" data-toggle=\"collapse\" class=\"collapsed\" " \
                              "aria-expanded=\"false\"><i class=\"accordion-indicator ti-angle-down\"></i></a>".format(parent.id)
                categories += "</h5>"

                categories += "<div class=\"collapse\" id=\"category_{}\" data-parent=\"#shop-categories\">".format(parent.id)
                categories += "<div class=\"card-body\">"
                categories += "<div class=\"inner_widget_link\">"
                categories += "<ul>"
                categories += self.sub_categories(parent, parent.slug)
                categories += "</ul></div></div></div>"
            else:
                categories += "<h5><a href=\"/{}/\" class=\"collapsed\">{}</a></h5>".format(parent.slug, parent.name)
            categories += "</div>"

        return categories

    def sub_categories(self, parent, parent_slug):
        sub_categories = "<div id=\"shop-sub-categories_{}\">".format(parent.slug)
        child_slug = parent_slug

        for child in parent.parent_category.all():
            sub_categories += "<div class=\"single_filter_card\">"

            if child.parent_category.count() > 0:
                sub_categories += "<h5>"
                sub_categories += "<a href=\"/{}/{}/\" role=\"button\" " \
                                  "class=\"collapsed\">{}</a>".format(child_slug, child.slug, child.name)
                sub_categories += "<a href=\"#category_{}\" data-toggle=\"collapse\" class=\"collapsed\" " \
                                  "aria-expanded=\"false\"><i class=\"accordion-indicator ti-angle-down\">" \
                                  "</i></a>".format(child.id)
                sub_categories += "</h5>"

                sub_categories += "<div class=\"collapse\" id=\"category_{}\" " \
                                  "data-parent=\"#shop-sub-categories_{}\">".format(child.id, parent.slug)
                sub_categories += "<div class=\"card-body\">"
                sub_categories += "<div class=\"inner_widget_link\">"
                sub_categories += "<ul>"
                child_slug += "/{}".format(child.slug)
                sub_categories += self.sub_categories(child, child_slug)
                sub_categories += "</ul></div></div></div></div>"
                child_slug = parent_slug
            else:
                sub_categories += "<li><a href=\"/{}/{}/\">{}</a></li>".format(parent_slug, child.slug, child.name)
        sub_categories += "</div>"

        return sub_categories

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.kwargs['slug']
        context['header_categories'] = generate_category()
        category_obj = get_object_or_404(Category, slug=self.kwargs['slug'], status=True)
        context['sub_categories'] = self.category()
        context['categories'] = category_obj

        return context
