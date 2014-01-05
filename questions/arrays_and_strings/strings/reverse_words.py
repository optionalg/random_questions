def reverse_words(sentence):
  '''
  take words in a sentence, and reverse the order of the words by walking along each
  character and rebuilding words, ending at spaces
  '''
  new_sentence = ''
  word = ''
  for character in sentence:
    if character == ' ':
      # when a space is it, prepend the saved word to the new sentence 
      # this prepending effectively reverses the order 
      new_sentence = word + new_sentence
      if new_sentence != '':
        # as long as the new_sentence isn't blank, add a space in front of it
        new_sentence  = ' ' + new_sentence
      # make room for a new word!
      word = ''
    else:
      # build the word one character at a time
      word += character
  # collect any word at the end of the sentence and prepend
  new_sentence = word + new_sentence

  return new_sentence




