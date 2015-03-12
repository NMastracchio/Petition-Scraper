import json
import re
import ast
from sys import argv
from pprint import pprint

script, sFilename = argv

with open(sFilename) as json_data:
	
	lPetitions = ast.literal_eval(json_data.read()[:-1])
	for dDict in lPetitions:
		for key, item in dDict.iteritems():
			if(key == "description"):
				lTerms = [r'(?P<marijuana>[Cc]annabis)', r'(?P<gay>LGBT)']
				for items in lTerms:
					sMatch = re.search(items, item[0])
					if sMatch:
						print sMatch.groupdict()