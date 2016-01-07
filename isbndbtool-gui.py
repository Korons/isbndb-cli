import argparse
import urllib
import sys
import json
from gooey import Gooey
from gooey import GooeyParser
@Gooey      
def main():
	parser = argparse.ArgumentParser(description='Get metadata for a book')
	parser.add_argument("-k", help="Your isbndb apikey")
	parser.add_argument("-t", help="Book title or isbndb book_id")
	parser.add_argument("-r", help="raw XML/JSON/YAML", choices=['JSON','XML','YAML'])
	parser.add_argument("-c", help="Collections type", choices=['book','books','author','authors'])
	parser.add_argument("-q", help="Keyword to search")
	parser.add_argument("-i", help="Index to search", choices=['author_id' , 'author_name','publisher_id'
		,'publisher_name','book_summary','book_notes','dewey','lcc','combined','full'])

	args = parser.parse_args()

	params = {}
	keys = ['q']


	if args.q:
		for k in keys:
  			if args.__getattribute__(k): params[k] = args.__getattribute__(k)

		if len(params) == 0:
  			parser.print_usage()
  			sys.exit()

	apicall = urllib.urlopen('http://isbndb.com/api/v2/json/' + args.k + '/books?%s' % urllib.urlencode(params))
	result = apicall.read()
	apicall.close()

	if args.t:

		#we have to replace spaces wiht _ because isbndb doesn't return info if you just url encode
		title = args.t
		title = title.replace(' ','_')
		url = "http://isbndb.com/api/v2/json/" + args.k + "/book/" + title
		print url
		api_call = urllib.urlopen(url)
		result = api_call.read()

	# print raw output and exit, if raw output was requested
	if args.r:
		url = "http://isbndb.com/api/v2/" + args.r + "/" + args.k + "/book/" + title
		print result
		sys.exit()

	chars_to_remove = ['"', '[', ']','}']
	result = result.translate(None, ''.join(chars_to_remove))
	result = result.replace(',', '\n')
	result = result.replace('{','\n\n\n')
	print result

if __name__ == '__main__':
	main()