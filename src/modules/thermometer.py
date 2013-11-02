import actions
import ECA_parser
import fm

def init(arg):
	pass

#Update een thermometer gadget, waarvan de id gegeven is, met een nieuwe splitwaarde.
def update_thermometer(gadget_id, split):
	return actions.update_thermometer(gadget_id, split)

ECA_parser.functions.update({ "updateThermometer": (2, fm.fcall2(update_thermometer)) })