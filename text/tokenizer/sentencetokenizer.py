import re

from tokenizer import Tokenizer

"""
Class to tokenize paragraphs into sentences
TODO: base this class on the lines of StreamTokenizer.java
[http://suif.stanford.edu/~mhn/deadlock/elevator/java/io/StreamTokenizer.java.html]
"""
class SentenceTokenizer(Tokenizer):

        def __init__(self):
		Tokenizer.__init__(self)

	def tokenize(self, data):
		return re.split(r'[.:]+', data)

if __name__ == '__main__':
	# USAGE
	t = SentenceTokenizer()
	print t.tokenize('this is a test. Only a test [yeah right].')

