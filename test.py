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

def getData(filename):
   """ Return metadata and documents from filename """

   f = open(filename)
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

      termFrequency = {}

      for word in r['text'].split():
         word = stripWord(word)
         word = word.lower()

         # in case a word is just made up of punctuation like !!
         if not word:
            continue
         
         if word not in stopwords:
            word = porter.stem(word, 0, len(word) - 1)
            termFrequency[word] = termFrequency.get(word, 0) + 1
      
      documents.append(termFrequency)

      return metadata, documents


def getVocab(documents):
   """ Generate the vocabulary from the given documents """

   vocabulary = {}

   for termFrequencies in documents:

      for term in termFrequencies:
         # update document frequencyi for each term
         vocabulary[term] = vocabulary.get(term,0) + 1
   return vocabulary


def generateTfAndIdf(documents, vocabulary):
   """ Compute term frequency * inverse document frequency """

   numOfDocuments = len(documents)
   for termFrequencies in documents:
      # find the max frequency in the document
      maxFrequency = 0
      for term in termFrequencies:
         freq = termFrequencies[term]
         if freq > maxFrequency:
            maxFrequency = freq

      for term in termFrequencies:
         tf = termFrequencies[term] / maxFrequency
         idf = log(numOfDocuments / vocabulary[term],2)
         termFrequencies[term] = tf * idf


if __name__ == '__main__':   
   rawdata = 'input.json' 
   metadata, documents = getData(rawdata)
   vocabulary = getVocab(documents)
   generateTfAndIdf(documents, vocabulary)