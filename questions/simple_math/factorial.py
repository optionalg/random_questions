# implement the factorial operator using a while loop and (separately) using recursion

def factorial_while(n):
  '''
  decrement n and multiply result by current product
  '''
  if n < 0:
    return False
  else:
    p = 1
    while n > 1:
      p = p*n
      n -= 1
  return p

def factorial_recursion(n):
  '''
  recursively call this function and multiply result by previous results
  '''
  if n < 0:
    return False
  else:
    if n <= 1:
      return 1
    else:
      return n*factorial_recursion(n-1)