# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from hurl.models import Url
from hurl.typos import get_typos, get_layouts, get_typos_forlayout
from hurl.statcont import get_content
from django import forms
from captcha.fields import CaptchaField
from django.template import RequestContext

def index(request, pgname):
  allurls = Url.objects.all()
  layouts = get_layouts()
  maincont = get_content(pgname)
  return render_to_response("index.html", {"allurls": allurls,
    "layouts":layouts, "content": maincont})

def view_layout(request, layout):
  allurls = Url.objects.all()
  return render_to_response("locale.html", {"allurls": allurls, "layout": layout})

def show_url(request, layout, url_name): # show url
  try:
    url = Url.objects.get(pk = url_name)
    urlname = url.urlname
    typos = []
    get_typos_forlayout(urlname, layout, typos)
    return render_to_response("site.html", {"urlname": urlname, "layout": layout, "typos": typos})
  except Url.DoesNotExist:
    return HttpResponse("The URL name %s does not exists!"%url_name)
  return HttpResponse(res)

class CaptchaForm(forms.Form):
  captcha = CaptchaField()

def create_url(request, url_name): #create url
  urlname = url_name
  try:
    urlname = Url.objects.get(pk = url_name)
    return HttpResponse("The URL name %s already exists!"%url_name)
  except Url.DoesNotExist:
    pass
  if request.POST:
    form = CaptchaForm(request.POST)
    if form.is_valid():
      url = Url(urlname = url_name)
      url.save()
      return HttpResponse("The URL name %s has been added successfully."%url_name)
      #return render_to_response("create.html", {"urlname":url_name}, context_instance=RequestContext(request))
  else:
    form = CaptchaForm()
  return render_to_response('create.html',locals(), context_instance=RequestContext(request)) 


import re
def add_url_file(request, addfile):
  fname = "/home/hurlpr/%s"%addfile
  try:
    f = open(fname)
  except:
    return HttpResponse("The file %s does not exists!"%addfile)
  response = HttpResponse()
  valid = re.compile("^[\.\-\w]+\.[a-z]{1,4}$")
  for urln in f:
    urln = urln.strip()
    if urln == "":
      continue
    try:
      urlname = Url.objects.get(pk = urln)
      response.write("The URL name %s already exists :/</br>"%urln)
      continue
    except:
      pass
    if valid.match(urln):
      url = Url(urlname = urln)
      url.save()
      response.write("The URL %s was added :)</br>"%urln)
    else:
      response.write("The URL %s was invalid :(</br>"%urln)
  return response

"""
from django.views.generic.edit import CreateView
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url
import json

class AjaxCaptchaForm(CreateView):
  template_name = ''
  form_class = AjaxForm

  def form_invalid(self, form):
    if self.request.is_ajax():
      to_json_responce = dict()
      to_json_responce['status'] = 0
      to_json_responce['form_errors'] = form.errors

      to_json_responce['new_cptch_key'] = CaptchaStore.generate_key()
      to_json_responce['new_cptch_image'] = captcha_image_url(to_json_responce['new_cptch_key'])

      return HttpResponse(json.dumps(to_json_responce), content_type='application/json')

  def form_valid(self, form):
    form.save()
    if self.request.is_ajax():
      to_json_responce = dict()
      to_json_responce['status'] = 1

      to_json_responce['new_cptch_key'] = CaptchaStore.generate_key()
      to_json_responce['new_cptch_image'] = captcha_image_url(to_json_responce['new_cptch_key'])

      return HttpResponse(json.dumps(to_json_responce), content_type='application/json')
"""
