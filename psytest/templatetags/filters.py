from django import template

register = template.Library()


@register.filter()
def rangesBai(count=21):
    return range(1, count)
