def upper_and_lower(txt):
  solution = {
    'uppers':0,
    'lowers':0,
  }
  
  for char in txt:
    if char.isupper():
      solution['uppers']+=1
    elif char.islower():
      solution['lowers']+=1
    else:
      pass

  return solution


txt = upper_and_lower(raw_input())
print txt['uppers']
print txt['lowers']
