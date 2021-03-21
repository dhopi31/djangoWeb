from django import template
import locale

register = template.Library()

@register.filter
def rupiah_format(angka, desimal=2):
    locale.setlocale(locale.LC_NUMERIC, 'IND')
    rupiah = locale.format("%.*f", (desimal, angka), True)
    return "Rp. {}".format(rupiah)
