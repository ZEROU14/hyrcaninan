from django import template

register = template.Library()

@register.filter
def translate_number(number):
    number = str(number)
    e_to_p_table = number.maketrans('0123456789','۰۱۲۳۴۵۶۷۸۹')
    return number.translate(e_to_p_table)
    