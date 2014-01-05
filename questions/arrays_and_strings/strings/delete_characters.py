def delete_characters(string, letters_to_delete):
  '''
  given a string, delete each instance of the characters given letters_to_delete
  '''
  for letter in letters_to_delete:
    string = string.replace(letter, '')
  return string

def delete_characters_no_replace(string, letters_to_delete):
  '''
  given a string, delete each instance of the characters given to_delete
  without using the builtin method .replace(). In this case, we consider the string
  a Queue and iterate through the string: if each leading letter is good, we put it back in 
  the Queue, if it is bad we remove it. Iteration starts when we've iterated
  through the length of the original string
  '''
  if len(string) > 1:
    for i in range(len(string)):
      if string[0] not in letters_to_delete:
        # if the leading letter is not bad, move it to the back of the string
        string = string[1:] + string[0]
      else:
        # else, remove it from the string
        string = string[1:]
  else:
    if string[0] in letters_to_delete:
      # if the string is only one letter, there's only one thing to check
      string = ''
  return string
