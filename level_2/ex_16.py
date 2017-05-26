import math


def square_odd_number(list_of_numbers):
  
  list_odd_numbers_squared=[int(odd_number)**int(odd_number) for odd_number in list_of_numbers if int(odd_number)%2==1]

  return list_odd_numbers_squared



print square_odd_number(raw_input().split(','))
