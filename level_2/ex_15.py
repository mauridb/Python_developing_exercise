def calc(n):
  
  formula = {
    'first':n,
    'second':n+n,
    'third':n+n+n,
    'fourth':n+n+n+n,
  }
  
  result = formula['first']+','+formula['second']+','+formula['third']+','+formula['fourth']
  l = [formula[key] for key in formula]
  tot = 0
  for i in l:
    i = int(i)
    tot += i

  return tot




number = raw_input()
print calc(number)
