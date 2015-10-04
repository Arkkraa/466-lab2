import json
import pprint
import string

def create_words_data(results):
	words_file = dict()
	i = 0

	for r in results:
		text = r['text'].split()
		text = [word.strip(string.punctuation) for word in text]
		words = {'pid': r['pid'], 'text': text}
		if words not in words_file.values():
			words_file[i] = words
		i += 1

	#pprint.pprint(words_file)
		
def main():
	fp = open("SB277Utter.json", 'r+')
	results = json.loads(fp.read())
	create_words_data(results)

if __name__ == '__main__':
	main()