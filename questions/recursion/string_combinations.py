# create a function that returns all combinations of letters in a string
# 12 and 21 are considered the same combination 

def combinate(string, prefix='', combos=[]):
  '''
  return a list of all combinations of letters in string, two combinations
  that differ only in order are not considered unique
  '''
  for i in range(len(string)):
    new_combo = prefix + string[i] 
    combos.append(new_combo)
    if len(string) > 1:
      combos = combinate(string[(i+1):], new_combo, combos)
  return combos

