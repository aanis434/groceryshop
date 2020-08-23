from products.models import Category


def generate_category():
    parent_category = Category.objects.filter(parent_id=None, status=True)
    categories = ''

    for parent in parent_category:
        if parent.parent_category.count() > 0:
            categories += "<li class=\"u-has-submenu u-header-collapse__submenu\">" \
                          "<a class=\"u-header-collapse__nav-link u-header-collapse__nav-pointer\" " \
                          "href=\"javascript:;\" role=\"button\" data-toggle=\"collapse\" " \
                          "aria-expanded=\"false\" aria-controls=\"headerSidebarHomeCollapse\" " \
                          "data-target=\"#header_category_" + str(parent.id) + "\">" + parent.name + "</a>" \
                          "<div id=\"header_category_"+str(parent.id)+"\" class=\"collapse\" " \
                          "data-parent=\"#headerSidebarContent\">" \
                          "<ul id=\"headerSidebarHomeMenu\" class=\"u-header-collapse__nav-list\">" \
                          "<li><a class=\"u-header-collapse__submenu-nav-link\" href=\"../home/index.html\">"\
                          + parent.name + "</a></li></ul></div></li>"
        else:
            categories += "<li><a class=\"u-header-collapse__submenu-nav-link\" " \
                          "href=\"../home/index.html\">" + parent.name + "</a></li>"

    return categories
