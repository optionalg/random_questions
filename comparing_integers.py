# Write a function that compares two integers without using a comparison operator

# Solution 1: Using a dict and try/except
def compare_ints(a, b):
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

print compare_ints(0,0)