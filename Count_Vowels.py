s = raw_input("Enter word\n").lower()

def countvowels(s):
	total = 0
	for letter in s:
		for vowel in "aeiou":
			if letter == vowel:
				total += 1
	return total

print s + " has " + str(countvowels(s)) + " vowels."
