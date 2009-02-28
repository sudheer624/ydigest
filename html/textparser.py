from HTMLParser import HTMLParser

class TextParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.data = []
		self.appendDataFlag = False

	def handle_starttag(self, tag, attrs):
		self.appendDataFlag = True

	def handle_endtag(self, tag):
		self.appendDataFlag = False
	
	def handle_data(self, data):
		self.data.append(data)

	def getData(self):
		return ''.join(self.data)

if __name__ == "__main__":
	parser = textparser()
	parser.feed("<html><body>this is a test</body></html>")
	print "%s" % parser.getData()
