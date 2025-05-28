from django import template

register = template.Library()

@register.filter
def currency_br(value):
    try:
        value = float(value)
    except (TypeError, ValueError):
        return value
    formatted = f"{value:,.2f}".replace(",", "v").replace(".", ",").replace("v", ".")
    return f"{formatted}"
