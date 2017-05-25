def calc_letters_and_numbers(sentence):
  solution = {
    'letters':0,
    'numbers':0,
  }
  for char in sentence:
    if char.isalpha():
      solution['letters'] += 1 
    elif char.isdigit():
      solution['numbers'] += 1
    else:
      pass
  return solution 


solution = calc_letters_and_numbers(raw_input())
print 'LETTERS: '+str(solution['letters'])
print 'NUMBERS: '+str(solution['numbers'])
