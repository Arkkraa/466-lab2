import json
import pprint

def model_data():
	with open('parsed_text.json', 'r+') as fp:
		data = {int(key): value for key, value in json.load(fp).items()}


	term_freq = dict()
	for key, value in data.items():
		
	#pprint.pprint(data)

if __name__ == '__main__':
	model_data()