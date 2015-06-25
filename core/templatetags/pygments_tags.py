from django import template

from pygments.formatters import HtmlFormatter


register = template.Library()


@register.simple_tag()
def pygments_css():
    return HtmlFormatter().get_style_defs('.codehilite')
