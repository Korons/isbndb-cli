import argparse
import urllib
import sys
import json

parser = argparse.ArgumentParser(description='Get metadata for a book')

parser.add_argument("-k", help="Your isbndb apikey")
parser.add_argument("-t", help="Book title")
parser.add_argument("-r", help="raw XML/JSON", choices=['JSON','XML','YAML'])
parser.add_argument("-c", help="Collections type", choices=['book','books','author','authors']) # not implented yet

args = parser.parse_args()

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
sys.exit()
