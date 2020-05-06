def DNA_strand(dna):	#my solution
	dna_copy = ""
	for x in dna:
		if x == 'A':
			x = 'T'
			dna_copy += x
		elif x == 'T':
			x = 'A'
			dna_copy += x
		elif x == 'C':
			x = 'G'
			dna_copy += x
		elif x == 'G':
			x = 'C'
			dna_copy += x
	
	return dna_copy

def DNA_strand(dna):	#better solution
    return dna.translate(string.maketrans("ATCG","TAGC"))
