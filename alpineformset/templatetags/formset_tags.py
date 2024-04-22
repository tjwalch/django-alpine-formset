import re

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.inclusion_tag("alpineformset/formset-x-data.js")
def formset_x_data(formset):
    formset.management_form.fields['TOTAL_FORMS'].widget.attrs['x-model'] = 'TOTAL_FORMS'
    return {
        'total_form_count': formset.total_form_count(),
        'initial_form_count': formset.initial_form_count() + formset.extra,
    }


@register.tag
def emptyform(parser, token):
    nodelist = parser.parse(('endemptyform',))
    parser.delete_first_token()
    return EmptyFormNode(nodelist)


class EmptyFormNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        output = self.nodelist.render(context)
        output = re.sub(r'(name|id)=\"([\w-]+)__prefix__([\w-]+)\"',
                        ":\g<1>=\"'\g<2>'+i+'\g<3>'\"", output)
        output = f'<template x-for="(i, index) in extraForms" :key="index">{output}</template>'
        return output


@register.simple_tag
def alpine_js():
    return mark_safe(
        '<script defer src="https://cdn.jsdelivr.net/npm/alpinejs@3.x.x/dist/cdn.min.js"></script>'
    )
