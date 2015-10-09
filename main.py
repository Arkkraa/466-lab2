
import ir
import query_utils
import json

if __name__ == '__main__':
   # load saved model
   metadata, documents, vocabulary, ogText = ir.loadSystem()


   while True:
      query = raw_input('Your query (Enter to quit): ')
      if not query:
         break

      queryVector = query_utils.queryVectorFromString(query)
      query_utils.updateWeights(queryVector, vocabulary)
      similarities =  query_utils.cosineSimilarity(queryVector, documents)
      results = query_utils.getTopTen(similarities)

      for result in results:
         print ogText[result[0]]
         print "cosine: " + str(result[1])
         print

      print '\n' + 80 * '*'
