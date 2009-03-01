import string

from analyzer import Analyzer

"""
Class represents the lowercase analyzer
"""
class LowercaseAnalyzer(Analyzer):

	def process(self, data):
		return string.lower(data)

if __name__ == '__main__':
	# USAGE
	lc = LowercaseAnalyzer()
	print lc.analyze("THIS IS A TEST")
