def bank_transactions(flag,amount_of_money):
  amount_of_bank_account = 0
  
  if flag == 'deposit':
    amount_of_bank_account += amount_of_money
  
  elif flag == 'withdraw':
    amount_of_bank_account -= amount_of_money
  
  else:
    print 'please choose an operation: - deposit or withdraw'
  
  return amount_of_bank_account
  
print 'Istructions:\n1 - type "deposit" or "witdhraw"?\n2 - type the amount of money\n type "exit to turnoff the programm.."'

tot = 0
while True:

  init_transaction = raw_input()
  if not init_transaction:
    break

  tot += bank_transactions(init_transaction, int(raw_input()))

print tot
