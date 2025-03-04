from django import template

register = template.Library()

@register.filter(name='dictvalue')
def dictvalue(value, dict_string):
    """
    Bu filter tanlangan statusni qulay shaklda ko'rsatadi.
    """
    dict_items = dict_string.split(',')
    dict_dict = {item.split('=')[0]: item.split('=')[1] for item in dict_items}
    return dict_dict.get(value, value)
