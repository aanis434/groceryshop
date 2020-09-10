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
        pathinfo = self.request.path_info.strip('/').split('/')
        categories = ''
        parent_category = Category.objects.filter(parent_id=None, status=True)

        for parent in parent_category:
            categories += "<div class=\"single_filter_card\">"
            class_value = "collapsed"
            aria_value = "false"
            div_class = ""

            if parent.slug in pathinfo:
                class_value = ""
                aria_value = "true"
                div_class = "show"

            if parent.parent_category.count() > 0:
                # print("parent", parent.id)
                categories += "<h5>"
                categories += "<a href=\"/{}/\" role=\"button\" class=\"{}\">{}</a>".format(parent.slug, class_value, parent.name)
                categories += "<a href=\"#category_{}\" data-toggle=\"collapse\" class=\"{}\" " \
                              "aria-expanded=\"{}\"><i class=\"accordion-indicator ti-angle-down\"></i></a>".format(parent.id, class_value, aria_value)
                categories += "</h5>"

                categories += "<div class=\"collapse {}\" id=\"category_{}\" data-parent=\"#shop-categories\">".format(div_class, parent.id)
                categories += "<div class=\"card-body\">"
                categories += "<div class=\"inner_widget_link\">"
                categories += "<ul>"
                categories += self.sub_categories(parent, parent.slug, pathinfo)
                categories += "</ul></div></div></div>"
            else:
                categories += "<h5><a href=\"/{}/\" class=\"{}\">{}</a></h5>".format(parent.slug, class_value, parent.name)
            categories += "</div>"

        return categories

    def sub_categories(self, parent, parent_slug, pathinfo):
        sub_categories = "<div id=\"shop-sub-categories_{}\">".format(parent.id)
        child_slug = parent_slug

        for child in parent.parent_category.all():
            class_value = "collapsed"
            aria_value = "false"
            div_class = ""

            if child.slug in pathinfo:
                class_value = ""
                aria_value = "true"
                div_class = "show"

            if child.parent_category.count() > 0:
                sub_categories += "<div class=\"single_filter_card\">"
                sub_categories += "<h5>"
                sub_categories += "<a href=\"/{}/{}/\" role=\"button\" " \
                                  "class=\"{}\">{}</a>".format(child_slug, child.slug, class_value, child.name)
                sub_categories += "<a href=\"#category_{}\" data-toggle=\"collapse\" class=\"{}\" " \
                                  "aria-expanded=\"{}\"><i class=\"accordion-indicator ti-angle-down\">" \
                                  "</i></a>".format(child.id, class_value, aria_value)
                sub_categories += "</h5>"

                sub_categories += "<div class=\"collapse {}\" id=\"category_{}\" " \
                                  "data-parent=\"#shop-sub-categories_{}\">".format(div_class, child.id, parent.id)
                sub_categories += "<div class=\"card-body\">"
                sub_categories += "<div class=\"inner_widget_link\">"
                sub_categories += "<ul>"
                child_slug += "/{}".format(child.slug)
                sub_categories += self.sub_categories(child, child_slug, pathinfo)
                sub_categories += "</ul></div></div></div></div>"
                child_slug = parent_slug
            else:
                sub_categories += "<h5><a class=\"{}\" href=\"/{}/{}/\">{}</a></h5>".format(class_value, parent_slug, child.slug, child.name)
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
