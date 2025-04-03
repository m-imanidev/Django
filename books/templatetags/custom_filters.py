from django import template

register = template.Library()

@register.filter
def format_price(value):
    try:
        return f"{int(value):,}"
    except (ValueError, TypeError):
        return value
    
@register.filter
def discounted_price(price, discount):
    try:
        discount_amount = (int(price) * int(discount)) / 100
        return int(price) - discount_amount
    except (ValueError, TypeError):
        return price