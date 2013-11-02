import ECA_parser
import fm
import json

def init(arg):
	pass

#Gegeven een tweet object geeft het de 'media_url' terug indien deze aanwezig was in het json object van de tweet
def getmediaurl(tweet):
	url = ''
	try:
		j = tweet.data['json']
		url = json.loads(j)['entities']['media'][0]['media_url']
	except KeyError:
		pass
	
	return url

#Gegeven een tweet object geeft het de waarde van 'retweeted' terug uit het json object
def isretweeted(tweet):
	retweet = False
	try:
		j = tweet.data['json']
		retweet = json.loads(j)['retweeted']
	except KeyError:
		pass
	
	return retweet


parse_json_functions = {
	"getmediaurl": (1, fm.fcall1(getmediaurl)),
	"isretweeted": (1, fm.fcall1(isretweeted))
}

ECA_parser.functions.update( parse_json_functions )