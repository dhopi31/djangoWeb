from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()
import locale

@register.filter
@stringfilter
def rupiah_format(angka, with_prefix=False, desimal=2):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format("%.*f", (desimal, angka), True)
    if with_prefix:
        return "Rp. {}".format(rupiah)
    return rupiah