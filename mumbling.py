def accum(s):	#my solution
	index = 0
	times = 0
	new_s = ''
	for letter in s:
		if len(s) == (times + 1):
			new_s += (s[index].upper() + s[index].lower() * times)
			break
		new_s += (s[index].upper() + s[index].lower() * times + '-')
		index = index + 1
		times = times + 1
	return new_s

def accum(s):	#best solution
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
