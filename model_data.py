import json
import pprint
from porter_stem import *
import math

def get_inv_doc_frequencies(data, count):
	inv_doc_freq = dict()

	for key, value in data.items():
		inv_doc_freq[key] = math.log(count/value, 2)

def get_doc_count(data):
	return len(data)

def get_doc_frequencies(data):
	doc_freq = dict()

	for key, value in data.items():
		seen = []
		for word in value['text']:
			if word not in seen:
				if word not in doc_freq.keys():
					doc_freq[word] = 1
				else:
					doc_freq[word] += 1
				seen.append(word)

	return doc_freq

def get_term_frequencies(data):
	model = dict()

	for key, value in data.items():
		term_freq = dict()
		for word in value['text']:
			if word not in term_freq.keys():
				term_freq[word] = 1
			else:
				term_freq[word] += 1
		model[key] = term_freq

	return model

def stem_data(data):
	with open('stem.json', 'w') as stem:
		json.dump(data, stem, indent=0)

	porter_stem('stem.json')

	with open('stemmed.json', 'r') as stemmed:
		data = {int(key): value for key, value in json.load(stemmed).items()}

	return data

def remove_stop_words(data):
	stop_words = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am',
				  'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because',
				  'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by',
				  "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do',
				  'does', "doesn't", 'doing', "don't", 'down', 'during', 'each',
				  'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't",
				  'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her',
				  'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how',
				  "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into',
				  'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more',
				  'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off',
				  'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours',
				  'ourselves', 'out', 'over', 'own', 'same', "shan't", 'she',"she'd",
				  "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such',
				  'than', 'that', "that's", 'the', 'their', 'theirs', 'them',
				  'themselves', 'then', 'there', "there's", 'these', 'they',
				  "they'd", "they'll", "they're", "they've", 'this', 'those',
				  'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was',
				  "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't",
				  'what', "what's", 'when', "when's", 'where', "where's", 'which',
				  'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't",
				  'would', "wouldn't", 'you', "you'd", "you'll", "you're", 'your',
				  'yours', 'yourself', 'yourselves']

	removed_model = dict()
	for key, value in data.items():
		words = []
		new_dict = dict()
		for word in value['text']:
			if word.lower() not in stop_words:
				words.append(word)

		new_dict['pid'] = value['pid']
		new_dict['text'] = words
		removed_model[key] = new_dict

	return removed_model
	#pprint.pprint(removed_model)

def get_data():
	with open('parsed_text.json', 'r+') as fp:
		data = {int(key): value for key, value in json.load(fp).items()}

	return data

if __name__ == '__main__':
	data = get_data()
	data = remove_stop_words(data)
	data = stem_data(data)
	term_freq = get_term_frequencies(data)
	doc_freq = get_doc_frequencies(data)
	doc_count = get_doc_count(data)
	inv_doc_freq = get_inv_doc_frequencies(doc_freq, doc_count)









