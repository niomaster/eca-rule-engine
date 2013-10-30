import actions
import ECA_parser
import fm

def init(arg):
	pass

def update_thermometer(gadget_id, split):
	return actions.update_thermometer(gadget_id, split)

ECA_parser.functions.update({ "updateThermometer": (2, fm.fcall2(update_thermometer)) })