import json
import pprint
import porter_stem
import math
import operator

def get_tf_idf(idf, tf):
	tf_idf = {}

	for key, value in tf.items():
		max_cnt = 0
		doc = {}
		for word, cnt in value.items():
			if cnt > max_cnt:
				max_cnt = cnt
		for word, cnt in value.items():
			doc[word] = (cnt/float(max_cnt)) * idf.get(word)
		tf_idf[key] = doc
	return tf_idf

def get_inv_doc_frequencies(data, count):
	inv_doc_freq = dict()

	for key, value in data.items():
		inv_doc_freq[key] = math.log(count/value, 2)

	return inv_doc_freq

def get_doc_count(data):
	return len(data)

def get_doc_frequencies(data):
	doc_freq = dict()

	for key, value in data.items():
		seen = []
		for word in value['text']:
			if word not in seen:
				doc_freq[word] = doc_freq.get(word, 0) + 1
				seen.append(word)

	return doc_freq

def get_term_frequencies(data):
	model = dict()

	for key, value in data.items():
		term_freq = dict()
		for word in value['text']:
			term_freq[word] = term_freq.get(word, 0) + 1

		model[key] = term_freq

	return model

def getStopwords():
   """ Loads stopwords from file and returns a dictionary """
   stopwords = {}
   f = open('stopwords.txt', 'r')
   for line in f:
      line = line.strip()
      stopwords[line] = True
   return stopwords

def remove_and_stem(data):
	stopwords = getStopwords()
	stemmer = porter_stem.PorterStemmer()

	for key, value in data.items():
		words = []
		for word in value['text']:
			if word.lower() not in stopwords:
				words.append(stemmer.stem(word.lower(), 0 , len(word) - 1))

		data[key]['text'] = words

	return data





