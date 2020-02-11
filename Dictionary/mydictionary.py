
import json
import difflib
from difflib import get_close_matches

data = json.load(open("data.json"))

def search(word):
	try:
		meaning = data[word]
			
		print("\nThe meaning of the word '" + word + "' is :\n")
		for i in range(len(meaning)):
			print(str(i+1) + ". " + str(meaning[i]))
			
	except:
		match = get_close_matches(word, data.keys())
		if len(match) != 0:
			ch = input("\nDid you mean '" + str(match[0]) + "' ? y/n : ")
			if ch == 'y' or ch == 'Y':
				search(match[0])
			else:
				print("\nRequested word not found!")
		else:
			print("\nRequested word not found!")


while True:
	word = str(input("\nEnter a word to be searched\n(Type 'byebye' to end the program) :"))
	word = word.lower()
	
	if(word == 'byebye'):
		print("\nBye Bye!\n")
		break
	
	search(word)
	
	
	
	


