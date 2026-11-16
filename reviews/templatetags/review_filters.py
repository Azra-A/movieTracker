from django import template

register = template.Library()

@register.filter
def star_rating(value):
    try:
        stars = int(value)
        return '★' * stars + '☆' * (5 - stars)
    except (ValueError, TypeError):
        return value