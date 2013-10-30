import ECA_parser
import fm

def init(arg):
	pass

def filter_notgreater(dict, value):
	return { k: v for k, v in dict.items() if v > value }


ECA_parser.functions.update( { "filter_notgreater": (2, fm.fcall2(filter_notgreater)) } )