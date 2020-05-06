def getCount(inputStr):	#my solution
    num_vowels = 0
    for x in inputStr:
        if x is "a" or x is "e" or x is "i" or x is "o" or x is "u":
            num_vowels += 1
    
    return num_vowels

def getCount(s):	#best solution
    return sum(c in 'aeiou' for c in s)
