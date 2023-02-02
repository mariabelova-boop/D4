from django import template

register = template.Library()

@register.filter()
def currency(value):
    stopfilter = ["редиска", "морковка", "кабачок"]

    for word in value.split():
        if word.lower() in stopfilter:
            value = value.replace(word, f"{word[0]}{'*' * (len(word) - 1)}")
    return value

@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
   d = context['request'].GET.copy()
   for k, v in kwargs.items():
       d[k] = v
   return d.urlencode()

