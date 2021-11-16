# Palindrome Checker
'''
Palindromes are words that read the same backwards. 
For example: racecar, taco cat, eye, radar.
'''
try:
	def palindrome():
		word = input("Enter your word: ")
		word = word.casefold()
		rev_word = word[::-1]

		def res():
			restart = input("Would you like to try again? [yes/no]: ")
			if restart.lower() == 'yes':
				palindrome()
			elif restart.lower() == 'no':
				print("Thank you for using this application.")
			else:
				print("Please enter either yes or no.")
				res()

		if word == rev_word:
			print("This word is a palindrome.")
			res()
		elif word != rev_word:
			print("This word is not a palindrome.")
			res()
		else:
			print("There was an error. Please try again.")
			res()
	palindrome()
except:
	print("There was an error. Please try again.")
	res()