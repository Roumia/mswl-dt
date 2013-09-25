import urllib2
from bs4 import BeautifulSoup as Soup

def retrieve_url (url):

   """

  documantion

  """
   opener = urllib2.build_opener ()    

   try:
        t = opener.open (url).read ()
        parser = Soup(t)
        l =[x['href'] for x in parser.findAll ('a') \
                if x.has_attr ('href')]

        return l
   except urllib2.URLError: "if there is no network connection ,or the specified server doesn't exist "
      return []
   except ValueError:    "when a function receives an argument that has the right type but an inappropriate value of the url"
        return []
