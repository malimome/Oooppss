# -*- coding: utf-8 -*-

from layout import *
kmapfa = {"q":"ض", "w":"ص", "e":"ث", "r":"ق", "t":"ف", 
    "y":"غ", "u":"ع", "i":"ه", "o":"خ", "p":"ح", "a":"ش", "s":"س", "d":"ی",
    "f":"ب", "g":"ل", "h":"ا", "j":"ت", "k":"ن", "l":"م", "z":"ظ", "x":"ط", "c":"ز",
    "v":"ر", "b":"ذ", "n":"د", "m":"پ", ".":"."}

kmapar = {"q":"ض", "w":"ص", "e":"ث", "r":"ق", "t":"ف", 
    "y":"غ", "u":"ع", "i":"ه", "o":"خ", "p":"ح", "a":"ش", "s":"س", "d":"ي",
    "f":"ب", "g":"ل", "h":"ا", "j":"ت", "k":"ن", "l":"ن", "z":"ئ", "x":"ء",
    "c":"ؤ", "v":"ر", "b":"ﻻ", "n":"ى", "m":"ة"}

def get_typos_forlayout(urlname,layout, typos):
  """ 
      Get all typos for urlname in layout 
      typos is an array to fill in
  """
  misurl = unicode(urlname).decode("utf-8")
  urltypos = []
  if layout == "en-US":
    typos.append(urlname)
    return 0
  if layout not in keymaps:
    return 1
  kmaps = keymaps[layout]
  for kmap in kmaps:
    murl = misurl
    for k in kmap:
      #murl = murl.replace(k.decode("utf-8"), kmap[k].decode("utf-8"))
      murl = murl.replace(k, kmap[k])
    urltypos.append(murl)
  #misurl = misurl.encode("utf-8")
  for ut in urltypos:
    for i in range(3, len(ut)+1):
      typos.append(ut[:i])
  return 0

def get_typos(urlname, typos):
  """ Not used in this version """
  misurl = unicode(urlname).decode("utf-8")
  urltypos = []
  for km in keymaps:
    kmap = keymaps[km]
    murl = misurl
    for k in kmap:
      #murl = murl.replace(k.decode("utf-8"), kmap[k].decode("utf-8"))
      murl = murl.replace(k, kmap[k])
    urltypos.append(murl)
  #misurl = misurl.encode("utf-8")
  for ut in urltypos:
    for i in range(3, len(ut)+1):
      typos.append(ut[:i])
  return

def get_layouts():
  return keymaps.keys()


