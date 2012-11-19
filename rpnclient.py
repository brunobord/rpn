import rpn

rpn1 = rpn.RPN()

while(True):
	inpbuf = raw_input("> ")
	if inpbuf[:4] == "exit":
		break
	rpn1.send_input(inpbuf)
	print rpn1.get_stacktop()
