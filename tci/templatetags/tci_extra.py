from django.template.defaulttags import register

from django import template

register = template.Library()


def get_item(dictionary, key):
    print "--------------------"
    print dictionary
    print key
    print dictionary.get(key)
    return dictionary.get(key)

register.filter('get_item', get_item)
