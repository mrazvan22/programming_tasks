import numpy as np

def SWTriangle(n):
  '''
  Prints a south west triangle of size n
  :param n: size of triangle
  :return: None
  '''

  # scrie aici codul functiei

  pass

def NETriangle(n):
  '''
  Prints a north west triangle of size n
  :param n: size of triangle
  :return: None
  '''

  # scrie aici codul functiei

  pass

def MagicSquares(n):
  if n % 2 == 1:
    return oddOrder(n)
  elif n % 4 == 0:
    return doublyEvenOrder(n)
  else:
    return singlyEvenOrder(n)

def oddOrder(n):
  '''
  Creates and returns an odd-order magic square.
  :param n: size of magic square (n x n)
  :return:
  '''

  square = np.array((n,n), int)

  # scrie aici codul functiei

  return square

def doublyEvenOrder(n):
  '''
  Creates and returns an doubly-even magic square.
  :param n: size of magic square (n x n)
  :return:
  '''

  square = np.array((n,n), int)

  # scrie aici codul functiei

  return square

def singlyEvenOrder(n):
  '''
  Creates and returns an singly-even magic square.
  :param n: size of magic square (n x n)
  :return:
  '''

  square = np.array((n,n), int)

  # scrie aici codul functiei

  return square


