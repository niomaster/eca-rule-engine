import ECA_parser
import fm

def init(arg):
	pass

def module(name):
	return __import__(name)
	
ECA_parser.functions.update( { "module": (1, fm.fcall1(module)) } )