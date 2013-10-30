import actions
import ECA_parser
import fm

def init(arg):
	pass

def update_image(gadget_id, src):
	return actions.update_image(gadget_id, src)

ECA_parser.functions.update({ "updateImage": (2, fm.fcall2(update_image)) })