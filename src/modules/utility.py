import ECA_parser
import fm

def init(arg):
	pass

def map_max(dict, value):
	return { k: max(value, v) for k, v in dict.items() }


ECA_parser.functions.update( { "map_max": (2, fm.fcall2(map_max)) } )