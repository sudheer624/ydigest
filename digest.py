# initial hook to test the backend
# will need to write CGI interface here later

import urllib

from html.textparser import TextParser

from text.tokenizer.wordtokenizer import WordTokenizer

parser = TextParser()
data = urllib.urlopen('http://www.google.com').read()
parser.feed(data)
print parser.getData()
print "\n\n"
print WordTokenizer().tokenize(parser.getData())
