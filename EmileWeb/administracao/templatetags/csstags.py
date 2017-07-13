from django import template
import datetime
register = template.Library()


@register.filter(name='addcss')
def addcss(field, css):
   return field.as_widget(attrs={"class":css})


@register.filter(is_safe=True)
def label_with_classes(value, arg):
    return value.label_tag(attrs={'class': arg})


@register.filter(name='print_timestamp')
def print_timestamp(timestamp):
    try:
        ts = int(timestamp)
    except ValueError:
        return None
    return datetime.datetime.fromtimestamp(ts)
