import json
import pprint
import string
import re

def create_words_data(results):
	words_file = dict()
	i = 0

	for r in results:
		text = re.split(r'\s+|\.+', r['text'])
		text = [word.strip(string.punctuation) for word in text]
		text = [word for word in text if word != ""]
		words = {'pid': r['pid'], 'text': text}
		if words not in words_file.values():
			words_file[i] = words
		i += 1

	with open('parsed_text.json', 'w') as pt:
		json.dump(words_file, pt, indent=0)
		
def main():
	fp = open("SB277Utter.json", 'r+')
	results = json.loads(fp.read())
	create_words_data(results)

if __name__ == '__main__':
	main()