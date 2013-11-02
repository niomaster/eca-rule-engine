import ECA_parser
import fm

def init(arg):
	pass

#Gegeven een dictionary en een onderwaardegrens geeft het een dictionary terug met alleen de elementen waarvan de value groter was dan de gegeven waarde
def filter_notgreater(dict, value):
	return { k: v for k, v in dict.items() if v > value }


ECA_parser.functions.update( { "filter_notgreater": (2, fm.fcall2(filter_notgreater)) } )