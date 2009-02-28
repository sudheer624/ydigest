import string

from HTMLParser import HTMLParser

"""
Class for parsing text from html source
"""
class TextParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.data = []
		self.appendDataFlag = False

	def handle_starttag(self, tag, attrs):
		if tag == 'script' or tag == 'style':
			self.appendDataFlag = False

	def handle_endtag(self, tag):
		if tag == 'script' or tag == 'style':
			self.appendDataFlag = True
	
	def handle_data(self, data):
		if self.appendDataFlag:
			self.data.append(data)

	def getData(self):
		return ''.join(self.data)

if __name__ == "__main__":
	# USAGE
	parser = TextParser()
	parser.feed("<html><body>this is a test</body></html>")
	print "%s" % parser.getData()
