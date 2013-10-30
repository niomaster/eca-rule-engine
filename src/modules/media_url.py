import ECA_parser
import fm
import json

def init(arg):
	pass

def getmediaurl(tweet):
	url = ''
	try:
		j = tweet.data['json']
		print(json.loads(j)['entities']['media'][0]['media_url'])
	except KeyError:
		return ''
	
	return url


string_functions = {
	"getmediaurl": (1, fm.fcall1(getmediaurl))
}

ECA_parser.functions.update( string_functions )