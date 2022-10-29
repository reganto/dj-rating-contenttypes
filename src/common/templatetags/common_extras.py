from django import template

register = template.Library()


@register.simple_tag
def call_method(obj, method_name, *args):
    if hasattr(obj, method_name):
        method = getattr(obj, method_name)
        return method(*args)

    raise AttributeError(f"'{obj}' does not have '{method_name}'")
