def first_non_repeat(string):
  '''
  return the first character that is unique inside the passed string
  by checking the first letter with rest of string then moving it to the 
  back of the string if it is non unique
  '''
  result = None
  if len(string) == 1:
    # if the string has only 1 character, that character is unique!
    return string[0]
  else:
    for n in range(len(string)):
      first_letter = string[0]
      rest_of_string = string[1:]
      if first_letter in rest_of_string:
        string = rest_of_string + first_letter
      else:
        result = first_letter
        break
    return result

# OK, so the algorithm above works, but I've since realized that Python includes a count()
# method on strings... duh

def first_non_repeat_using_count(string):
  '''
  return the first letter that occurs only once in the string, starting from the beginning
  '''
  result = None
  for letter in string:
    if string.count(letter) == 1:
      result = letter
      break
  return result



