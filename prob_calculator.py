import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **kwargs):
    self.contents=list()
    for color, number in kwargs.items():
      if number > 1:
        for value in range(number):
          self.contents.append(color)
      else:
        self.contents.append(color)

  #def draw(self,number):
   # """Function that returns a list of the colors retrieved after Number of draws"""
    #if len(self.contents)<number:
     # return self.contents
    #else:
    #   return random.sample(self.contents, number)

  def draw(self, n):
    """Function that returns a list of the colors retrieved after Number of draws"""
    removed=[]
    if len(self.contents) < n: #In case the number is bigger than the amount of balls in the bag
      return self.contents
    for _ in range (n):
      removed.append(self.contents.pop(random.randrange(len(self.contents)))) #Pop is a method that subtracts an element from a list, randrange is a random number between 0 and the parameter of the method, this substracts a ball of the list randomly until n balls have been removed
    return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        another_hat = copy.deepcopy(hat) #The copy of the hat object
        balls_drawn = another_hat.draw(num_balls_drawn) #We make the experiment once
        balls_req = 0  # Initialize the count of required balls to 0
        for k, v in expected_balls.items():
        # For each color (k) and its expected quantity (v) in the expected_balls               dictionary
          count = balls_drawn.count(k)  # Count how many times the color appears in             balls_drawn
          if count >= v:
        # If the count of the color is greater than or equal to the expected quantity
            balls_req += 1  # Increment the count of required balls by 1
        m += 1 if balls_req == len(expected_balls) else 0
      
    return m / num_experiments
  
  
  
  
