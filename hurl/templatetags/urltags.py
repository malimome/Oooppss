from django import template
from django.template.defaultfilters import stringfilter
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.staticfiles import finders

register = template.Library()

@register.filter
@stringfilter
def image_exists(urlname):
  return True
  path = "/static/favicon/{0}.ico".format(urlname)
  #abspath = finders.find(path)
  if staticfiles_storage.exists(path):
    return True
  else:
    return False
