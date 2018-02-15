import math

def calc(a,b,c,d):
      
      if(type(a) == str):
            raise TypeError
      else:
            distance = math.sqrt((a-c)**2+(b-d)**2)
            return float("{0:.3f}".format(round(distance,3)))
