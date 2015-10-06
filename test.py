import json
import string
import stemmer

STOPWORDS_FILE = "stopwords.txt"

def getStopwords():
   """ Loads stopwords from file and returns a dictionary """
   stopwords = {}
   f = open(STOPWORDS_FILE)
   for line in f:
      line = line.strip()
      stopwords[line] = True
   return stopwords


def stripWord(word):
   """Generates a term based on the word given"""
   return word.strip(' ' + string.punctuation)

   

f = open('input.json')
records = json.loads(f.read())

metadata = []
documents = []

stopwords =  getStopwords()
porter = stemmer.PorterStemmer()

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
      word = stripWord(word)
      word = word.lower()

      # in case a word is just made up of punctuation like !!
      if not word:
         continue
      
      if word not in stopwords:
         word = porter.stem(word, 0, len(word) - 1)
         terms.append(word)

   documents.append(terms)

for d in documents:
   print d

