def array_dif(a, b):	#my solution
	for x in a:
		for x in b:
			try:
				a.remove(x)
			except ValueError:
				pass
	
	return a

def array_dif_1(a, b):	#best solution
	return [x for x in a if x not in b]
