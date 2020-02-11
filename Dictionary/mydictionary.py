
import json
import sys

data = json.load(open("data.json"))

def search(word):
    return data[word]

while True:
	word = str(input("\nEnter a word to be searched\n(Type 'byebye' to end the program) :"))
	
	if(word == 'byebye'):
		print("\nBye Bye!\n")
		break
	try:
		meaning = search(word)
		
		print("\nThe meaning of the word '" + word + "' is :\n")
		for i in range(len(meaning)):
			print(str(i+1) + ". " + str(meaning[i]))
			
	except:
		print("\nRequested word not found!\n")
	
	
	


