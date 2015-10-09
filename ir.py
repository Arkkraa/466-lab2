import json
import string
import stemmer
import math
import vector_utils, query_utils
import pickle

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
   return word.strip(string.punctuation)

def getData(filename):
   """ Return metadata and documents from filename """

   f = open(filename)
   records = json.loads(f.read())

   metadata = []
   documents = []
   ogText = []

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

      termFrequency = {}
      name = r['first'].lower()
      termFrequency[name] = 1

      for word in r['text'].split():
         word = stripWord(word)
         word = word.lower()

         # in case a word is just made up of punctuation like !!
         if not word:
            continue
         
         if word not in stopwords:
            word = porter.stem(word, 0, len(word) - 1)
            termFrequency[word] = termFrequency.get(word, 0) + 1
      
      if termFrequency not in documents:
         metadata.append(meta)
         documents.append(termFrequency)
         ogText.append(r['text'])

   
   return metadata, documents, ogText


def getVocab(documents):
   """ Generate the vocabulary from the given documents """

   vocabulary = {}

   for termFrequencies in documents:

      for term in termFrequencies:
         # update document frequencyi for each term
         vocabulary[term] = vocabulary.get(term,0) + 1
   return vocabulary

def generateIdf(vocabulary, numOfDocuments):
   """ Generate inverse document frequency for the given vocabulary """

   for term in vocabulary:
      inverse = float(numOfDocuments) / vocabulary[term]
      vocabulary[term] = math.log(inverse, 2)


def generateTf(documents, vocabulary):
   """ Compute term frequency * inverse document frequency. Vocab assumed to be in idf """

   for termFrequencies in documents:
      # find the max frequency in the document
      maxFrequency = 0
      for term in termFrequencies:
         freq = termFrequencies[term]
         if freq > maxFrequency:
            maxFrequency = freq

      for term in termFrequencies:
         tf = termFrequencies[term] / float(maxFrequency)
         idf = vocabulary[term]
         termFrequencies[term] = tf * idf

def saveSystem(metadata, documents, vocabulary, ogText):
   """ Persist the entire model """
   f = open("metadata.db", 'w')
   pickle.dump(metadata, f)
   f.close()

   f = open("documents.db", 'w')
   pickle.dump(documents, f)
   f.close()

   f = open("vocabulary.db", 'w')
   pickle.dump(vocabulary, f)
   f.close()

   f = open("ogText.db", 'w')
   pickle.dump(ogText, f)
   f.close()

def loadSystem():
   """ Returns the metadata, documents, and vocabulary ready to be used by the
   query engine """

   f = open('metadata.db')
   metadata = pickle.load(f)
   f.close()

   f = open('documents.db')
   documents = pickle.load(f)
   f.close()

   f = open('vocabulary.db')
   vocabulary = pickle.load(f)
   f.close()

   f = open('ogText.db')
   ogText = pickle.load(f)
   f.close()

   return metadata, documents, vocabulary, ogText


if __name__ == '__main__':   
   print 'creating the model...'
   # start up the system and create models
   #rawdata = 'input.json' 
   rawdata = 'SB277Utter.json'
   metadata, documents, ogText = getData(rawdata)
   print 'metadata:', len(metadata)
   print 'documents:', len(documents)
   vocabulary = getVocab(documents)
   generateIdf(vocabulary, len(documents))
   generateTf(documents, vocabulary)

   # save models to disk
   print 'saving the model...'
   saveSystem(metadata, documents, vocabulary, ogText)
   print 'done!'

