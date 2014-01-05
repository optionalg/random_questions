def delete_characters(string, letters_to_delete):
  '''
  given a string, delete each instance of the characters given letters_to_delete
  '''
  for letter in letters_to_delete:
    string = string.replace(letter, '')
  return string
