import urllib.request
import ECA_parser
import fm

def init(arg):
	pass

def getid(url):
	id = ''
	try:
		a = urllib.request.urlopen(url)
		r_url = a.geturl()
		if '://twitpic.com/' in r_url:
			id = r_url.split('/')[-1]
	except urllib.error.HTTPError:
		return ''
	
	return id

def getfull(url):
	id = getid(url)
	r = ''
	if id != '': 
		r = 'http://twitpic.com/show/full/' + id
	return r

def getthumb(url):
	id = getid(url)
	r = ''
	if id != '':
		r = 'http://twitpic.com/show/thumb/' + id
	return r


twitpic_functions = {
	"getid": (1, fm.fcall1(getid)),
	"getid": (1, fm.fcall1(getfull)),
	"getid": (1, fm.fcall1(getthumb))
}

ECA_parser.functions.update( twitpic_functions )