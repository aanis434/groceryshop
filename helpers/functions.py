from products.models import Category


def generate_category():
    parent_category = Category.objects.filter(parent_id=None, status=True)
    categories = ''

    for parent in parent_category:
        if parent.parent_category.count() > 0:
            categories += "<li class=\"u-has-submenu u-header-collapse__submenu\">" \
                          "<a class=\"u-header-collapse__nav-link u-header-collapse__nav-pointer\" " \
                          "href=\"javascript:;\" data-toggle=\"collapse\" " \
                          "aria-controls=\"headerSidebarHomeCollapse\" " \
                          "data-target=\"#header_category_" + str(parent.id) + "\">" + parent.name + "</a>" \
                          "<div id=\"header_category_"+str(parent.id)+"\" class=\"collapse\" " \
                          "data-parent=\"#headerSidebarContent\">" \
                          "<ul id=\"headerSidebarHomeMenu\" class=\"u-header-collapse__nav-list\">"

            categories += generate_sub_categories(parent)
            categories += "</ul></div></li>"
        else:
            categories += "<li><a class=\"u-header-collapse__submenu-nav-link\" " \
                          "href=\"/{}\">{}</a></li>".format(parent.slug, parent.name)

    return categories


def generate_sub_categories(parent):
    sub_categories = ''

    for child in parent.parent_category.all():
        if child.parent_category.count() > 0:
            sub_categories += "<li class=\"u-has-submenu u-header-collapse__submenu\">" \
                          "<a class=\"u-header-collapse__nav-link u-header-collapse__nav-pointer submenu\" " \
                          "href=\"javascript:;\" aria-controls=\"headerSidebarHomeCollapse\" " \
                          "data-target=\"#header_category_" + str(child.id) + "\">" + child.name + "</a>" \
                          "<div id=\"header_category_" + str(child.id) + "\" class=\"collapse\" " \
                          "data-parent=\"#headerSidebarContent\">" \
                          "<ul id=\"headerSidebarHomeMenu\" class=\"u-header-collapse__nav-list\">"

            sub_categories += generate_sub_categories(child)
            sub_categories += "</ul></div></li>"
        else:
            sub_categories += "<li><a class=\"u-header-collapse__submenu-nav-link\" href=\"../home/index.html\">" \
                          + child.name + "</a></li>"

    return sub_categories
