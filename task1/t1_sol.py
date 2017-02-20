import numpy as np

def quad(a,b,c,x):
  return a*x**2+b*x+c

def quadIsZero(a,b,c,x):
  return quad(a,b,c,x) == 0

def quadSolver(a,b,c):
  bigD = b**2 - 4*a*c

  if bigD < 0:
    return None
  else:
    x_1 = (-b - np.sqrt(bigD))/(2*a)
    x_2 = (-b + np.sqrt(bigD)) / (2 * a)

    return x_1, x_2

def toUpperCase(sentence):
  strList = sentence.split(' ')
  newList = []
  for word in strList:
    newWord = word[0].upper() + word[1:]
    newList = newList + [newWord]

  return ' '.join(newList)

def isPrime(n):
  for i in range(2,n):
    if n % i == 0:
      return False

  return True

def nextPrime(n):
  """
  Returns the smallest prime bigger than n
  """
  if isPrime(n+1):
    return n+1
  else:
    return nextPrime(n+1)

def primeFactorsHelper(n, k):
  print('n=%d, k=%d' % (n,k))
  if n == 1:
    return []
  elif n % k == 0:
    return [k] + primeFactorsHelper(n/k, k)
  else:
    return primeFactorsHelper(n, nextPrime(k))

def primeFactors(n):
  return primeFactorsHelper(n, 2)

def fib(n):
  if n == 1:
    return 1
  elif n == 2:
    return 1
  else:
    return fib(n-1) + fib(n-2)


def hanoi(n):
  if n == 0:
    return
  else:


# print(quad(1,2,0,1))
# print(quad(1,0,0,1))
#
#
# print(quadIsZero(1,2,0,1))
# print(quadIsZero(1,0,-1,1))

print(quadSolver(1, 2, 0), quadSolver(2, -4, 0), quadSolver(-2, -5, 4))

print(quadSolver(2, 4, 2))

print(toUpperCase('a very simple example'))