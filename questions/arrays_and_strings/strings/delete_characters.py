def delete_characters(word, to_delete):
  '''
  given a word delete each instance of the characters given to_delete
  '''
  for letter in to_delete:
    word = word.replace(letter, '')
  return word