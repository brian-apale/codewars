def is_isogram(string):
	y = []
	for x in string.lower():
		if x in y:
			return False
		y.append(x)
	return True



