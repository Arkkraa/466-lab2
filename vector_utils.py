# vector_utils assumes that a vector is represented as a dictionary; any element 
# not present is considered to have zero value 

import math

def dotProduct(v1, v2):
   """ Compute the dot product """
   result = 0
   for k in v1:
      result += v1[k] * v2[k]
   return result

def distance(vector):
   """ Compute the distance of a vector """
   result = 0
   for k in vector:
      result += vector[k] ** 2
   return math.sqrt(result)

def cosine(v1, v2):
   """ Compute the cosine of 2 vectors """
   top = dotProduct(v1, v2)
   distanceV1 = distance(v1)
   distanceV2 = distance(v2)

   return float(top) / (distanceV1 * distanceV2)





