from products.models import Category


def generate_category():
    parent_category = Category.objects.filter(parent_id=None, status=True)
    categories = ''

    for parent in parent_category:
        if parent.parent_category.count() > 0:
            categories += "<li class=\"active has-sub\"><a href=\"/{}/\">" \
                          "<span>{}</span></a>".format(parent.slug, parent.name)
            categories += "<ul>"
            categories += generate_sub_categories(parent, parent.slug)
            categories += "</ul></li>"
        else:
            categories += "<li><a href=\"/{}/\"><span>{}</span></a></li>".format(parent.slug, parent.name)

    return categories


def generate_sub_categories(parent, parent_slug):
    sub_categories = ''
    child_slug = parent_slug

    for child in parent.parent_category.all():
        if child.parent_category.count() > 0:
            sub_categories += "<li class=\"has-sub\"><a href=\"/{}/{}/\">" \
                          "<span>{}</span></a>".format(child_slug, child.slug, child.name)
            sub_categories += "<ul>"
            child_slug += "/{}".format(child.slug)
            sub_categories += generate_sub_categories(child, child_slug)
            sub_categories += "</ul></li>"
            child_slug = parent_slug
        else:
            sub_categories += "<li><a href=\"/{}/{}/\"><span>{}</span></a></li>".format(parent_slug, child.slug, child.name)

    return sub_categories
