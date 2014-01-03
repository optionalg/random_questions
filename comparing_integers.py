# Write a function that compares two integers without using a comparison operator

# Solution 1: Using a dict and try/except
def compare_ints_1(a, b):
  '''
  checks if two integers, a and b, are equal by dividing them and forcing a
  dict lookup of the result which will fail if it is anything other than 1
  '''
  d = {1.0 : True}
  try:
    c = float(a)/float(b)
    #this "float" business can be replaced with an import: "from __future__ import division"
  except:
    # if the division above fails, it might be beacuse b is zero, so I can add one
    # to each integer, which doesn't change their relative equality
    c = float(a+1)/float(b+1)
  try:
    # if a and be are the same, then c = 1.0, which is in d, otherwise an error is raised
    return d[c]
  except:
    return False

# Solution 2: Catching a division by 0 error as confirmation of equality
def compare_ints_2(a,b):
  '''
  checks if two integers, a and b, are equal by subtracting them then dividing
  an arbitrary integer by the result. If they are equal it should raise a 
  division by zero error
  '''
  try:
    d = 1.0/(a-b)
    return False
  except:
    return True
