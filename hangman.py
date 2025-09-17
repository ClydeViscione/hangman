User_input = input("Select a word: " )
Number_of_word = len(User_input)
underscore_space = '_' * Number_of_word

print ("The word :",underscore_space)
print ()


Live = int(Number_of_word)
Ask_for_letter = input("Enter: ")

while Live != 0:
	if Ask_for_letter in User_input:
		print ("The word: ", Ask_for_letter)
	elif Ask_for_letter not in User_input:
		Live = Live - 1
		print ("There's no",Ask_for_letter)
		print ("Live leftover: ",Live)
		print ("The word: " )
	elif Ask_for_letter == User_input:
		print ("U Win")
		break
	else:
		print ("U Loose")

