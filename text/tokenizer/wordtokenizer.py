import re

from tokenizer import Tokenizer

"""
Class to tokenize sentences into words
TODO: base this class on the lines of StreamTokenizer.java
[http://suif.stanford.edu/~mhn/deadlock/elevator/java/io/StreamTokenizer.java.html]
"""
class WordTokenizer(Tokenizer):

	def __init__(self):
		Tokenizer.__init__(self)

	def tokenize(self, data):
		return re.split(r'[ ,\t\.;:"\'-]+', data)

if __name__ == '__main__':
	# USAGE
	t = WordTokenizer()
	print t.tokenize('this is a test, and only a test [yeah right]')
