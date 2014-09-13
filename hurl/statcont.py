
def get_index():
  cnt = """If you are seeing this, it is possibly because you forgot to change the 
    keyboard layout while trying to access your favorite website.

    This service will simply redirect you to the right website even if you typed
    it by your local keyboard layout."""
  return cnt;

def get_about():
  cnt = """This is a website to redirect you to the right website if you typed the
  hostname wrong"""
  return cnt;

def get_copyright():
  cnt = "All rights reserved! 2013"
  return cnt;

def get_content(pgname):
  pages = {
      "": get_index, 
      "about": get_about, 
      "copyright": get_copyright,
    }
  if pgname not in pages:
    return ""
  return pages[pgname]()

