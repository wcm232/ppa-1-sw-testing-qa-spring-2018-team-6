import math

def calc(a,b,c,d):

      for argument in (a, b, c, d):
            if type(argument) != int and type(argument) != float:
                  return False
            
      distance = math.sqrt((a-c)**2+(b-d)**2)
      return float("{0:.3f}".format(round(distance,3)))

