# Util functions for query processing

from vector_utils import cosine
import ir
import stemmer

def updateWeights(queryVector, vocab):
   """ Compute weights using Salton Buckley algo. Vocab is assumed to be in
   inverse document frequency already"""

   maxFreq = 0
   for v in queryVector:
      freq = queryVector[v]
      if freq > maxFreq:
         maxFreq = freq

   for v in queryVector:
      freq = queryVector[v]
      queryVector[v] = (0.5 + (0.5 * freq) / maxFreq) * vocab[v]

def cosineSimilarity(queryVector, documents):
   """ Returns a list with the cosine similarity between the query and each
   document in the document collection """

   return map(lambda documentVector: cosine(queryVector, documentVector), documents)

def queryVectorFromString(query):
   """ Returns a query vector from input string.  Vector will contain frequency 
   counts. Function will remove stopwords and stem remainding query terms"""

   queryVector = {}
   stopwords =  ir.getStopwords()
   porter = stemmer.PorterStemmer()

   for word in query.split():
      word = ir.stripWord(word)
      word = word.lower()

      # in case a word is just made up of punctuation like !!
      if not word:
         continue
      
      # compute frequency of term
      if word not in stopwords:
         word = porter.stem(word, 0, len(word) - 1)
         queryVector[word] = queryVector.get(word, 0) + 1

   return queryVector

def getTopTen(lst):
   """ Returns the top ten query matches, along with the document index for future retrival """
   similarityWithIndex = list(enumerate(lst))
   return sorted(similarityWithIndex)[:10]

if __name__ == '__main__':
   query = raw_input("query: ")
   print queryVectorFromString(query)
   
