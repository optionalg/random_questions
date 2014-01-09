def permute(string, prefix = '', permutations = []):
  '''
  find every possible permutation of the string and return a list of all permutations
  '''
  if len(string) > 1:

    for i in range(len(string)):
      if i == 0:
        remaining_string = string[1:]
      else:
        remaining_string = string[:i] + string[(i+1):]
      permute(remaining_string, prefix + string[i])

  else:
    new_combination = prefix + string
    permutations.append(new_combination)

  return permutations
