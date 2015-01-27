s = raw_input("Enter Word\n").lower()

if s == s[::-1]:
	print s + " is a palidrome."
else:
	print s + " is not a palidrome."