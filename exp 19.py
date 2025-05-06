#Write a Python program that takes a sentence as input, removes punctuations from the sentence, and displays the modified sentence.
import re

def remove_punctuation(sentence):

	return re.sub(r'[^\w\s]','',sentence)
sentence = input().strip()

print(remove_puncuation(sentence))
