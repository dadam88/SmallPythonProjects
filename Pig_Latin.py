s = raw_input("Enter a word\n").lower()

def checkvowel(s):
	for vowel in "aeiou":
		if s[0] == vowel:
			return True
	
if checkvowel(s):
	print s + "way"

else:
	print s[1:] + s[0] + "ay"