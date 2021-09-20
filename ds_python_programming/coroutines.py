def complain_about(substring): 
	print("please talk to me") 
	try: 
		while True: 
			text = (yield)
			if substring in text: 
				print('Oh no: I found a %s again!'
                      % (substring))
	except GeneratorExit: 	
		print('Ok, ok: I am quitting.')
