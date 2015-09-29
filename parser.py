import json
import pprint

def create_meta_data(results):
	meta_data_keys = ['first', 'last', 'PersonType', 'date', 'house', 'Committee']
	meta_data_file = dict()
	for r in results:
		meta_data = dict()
		meta_data = {key:value for key, value in r.items() if key in meta_data_keys}
		meta_data_file[r['pid']] = meta_data

	f = open("meta_data.json", 'w+')
	json.dump(meta_data_file, f)

def main():
	fp = open("SB277Utter.json", 'r+')
	results = json.loads(fp.read())
	create_meta_data(results)

if __name__ == '__main__':
	main()