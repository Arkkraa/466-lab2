import json

f = open('input.json')
records = json.loads(f.read())

metadata = []
documents = []

for r in records:
   # extract people data 
   meta= {}
   meta['pid'] = r['pid']
   meta['first'] = r['first']
   meta['last'] = r['last']
   meta['PersonType'] = r['PersonType']
   meta['date'] = r['date']
   meta['house'] = r['house']
   meta['Committee'] = r['Committee']
   metadata.append(meta)

   documents.append(r['text'])

for d in documents:
   print d

