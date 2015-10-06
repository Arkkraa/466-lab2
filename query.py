import model_data
import json
import string
import pprint

def get_query_weights(query_freq, inv_doc_freq):
	query_weights = {}

	for query, freq in query_freq:
		query_weights[query] = freq * inv_doc_freq.get(query, 0)


def get_relevance(query_freq, tf_idf):
	"""num = 0
	docs = 0
	qs = 0
	"""
	

	for key, value in tf_idf:
		for word, tfidf in value:
			for query, freq in query_freq:
				num += tfidf * freq
			docs += tfidf ** 2

def get_query_freq(query):
	query_freq = {}

	for word in query:
		query_freq[word] = query_freq.get(word, 0) + 1

	return query_freq

if __name__ == '__main__':
	with open('parsed_text.json', 'r+') as fp:
		data = {int(key): value for key, value in json.load(fp).items()}

	data = model_data.remove_and_stem(data)
	term_freq = model_data.get_term_frequencies(data)
	doc_freq = model_data.get_doc_frequencies(data)
	doc_count = model_data.get_doc_count(data)
	inv_doc_freq = model_data.get_inv_doc_frequencies(doc_freq, doc_count)
	tf_idf = model_data.get_tf_idf(inv_doc_freq, term_freq)
	pprint.pprint(tf_idf)

	query = raw_input()
	query = query.split()
	query = [word.strip(string.punctuation) for word in query]
	query_freq = get_query_freq(query)
	#query_weights = get_query_weights(query_freq, inv_doc_freq)