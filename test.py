import json
import string

def stripWord(word):
   """Generates a term based on the word given"""
   return word.strip(' ' + string.punctuation)

   

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

   terms = []

   for word in r['text'].split():
      w = stripWord(word)
      if w:
         terms.append(w)
   documents.append(terms)

for d in documents:
   print d

