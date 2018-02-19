import math

def calculateDistance(coord1_x,coord1_y,coord2_x,coord2_y):

      for argument in (coord1_x, coord1_y, coord2_x, coord2_y):
            if type(argument) != int and type(argument) != float:
                  return False
            
      distance = math.sqrt((coord1_x-coord2_x)**2+(coord1_y-coord2_y)**2)
      return float((round(distance,3)))

