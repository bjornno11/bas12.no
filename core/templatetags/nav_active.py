from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def active(context, *namespaces):
    request = context.get('request')
    match = getattr(request, 'resolver_match', None)
    ns = (match.namespace or '') if match else ''
    return 'active' if any(ns.startswith(n) for n in namespaces) else ''
