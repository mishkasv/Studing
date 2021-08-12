from django import template

register = template.Library()


@register.filter(name='elided_range')
def get_elided_range_by_number(objects, page):
    page_range = objects.get_elided_page_range(page)
    return page_range
