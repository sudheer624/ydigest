# initial hook to test the backend
# will need to write CGI interface here later

import urllib

from html.textparser import TextParser

parser = TextParser()
data = urllib.urlopen('http://www.google.com').read()
parser.feed(data)
print parser.getData()
