import json
import pprint

def model_data():
	with open('parsed_text.json', 'r+') as fp:
		data = {int(key): value for key, value in json.load(fp).items()}

	model = dict()
	for key, value in data.items():
		term_freq = dict()
		for word in value['text']:
			if word not in term_freq.keys():
				term_freq[word] = 1
			else:
				term_freq[word] += 1
		model[key] = term_freq

	
	
	#pprint.pprint(model)

if __name__ == '__main__':
	model_data()