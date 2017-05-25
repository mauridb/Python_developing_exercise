def remove_double(list_elem):
  list_new = []

  for elem in list_elem:
    if elem not in list_new:
      list_new.append(elem)

  return list_new

#______________________________________


def remove_duplicate_word_from_input_text(sentence):
  sentence = sentence.split()
  sentence.sort()
  solution = remove_double(sentence)
  return ' '.join(solution)



  
sentence = raw_input()
print remove_duplicate_word_from_input_text(sentence)
