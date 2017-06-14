from t1_sol import *
import unittest

############## HELPER FUNCTIONS ###################

def checkListsEqual(l1,l2):
  return len(l1) == len(l2) and sorted(l1) == sorted(l2)

def checkListsAlmostEqual(l1,l2):
  return np.linalg.norm(np.array(l1) - np.array(l2)) < 0.01

############### UNIT TESTS ######################

def test_quad():
  assert quad(1, 2, 0, 1) == 3
  assert quad(1, 0, 0, 1) == 1
  assert quad(1, 2, 4, 1) == 7
  assert quad(0, 4, -2, 1) == 2


def test_quadIsZero():
  assert quadIsZero(1,2,0,1) == False
  assert quadIsZero(1, 0, -1, 1) == True
  assert quadIsZero(0, 0, -5, 5) == False


def test_quadSolver():
  assert quadSolver(1, 2, 0) == (-2.0,0.0)
  assert quadSolver(2, -4, 0) == (0.0, 2.0)
  assert checkListsAlmostEqual(quadSolver(-2, -5, 4), (0.637, -3.137))
  assert quadSolver(10, 4, 2) is None
  assert checkListsAlmostEqual(quadSolver(2, 4, 2), (-1, -1))

def test_toUpperCase():
  assert toUpperCase('a very simple example') == 'A Very Simple Example'
  assert toUpperCase('ana are mere') == 'Ana Are Mere'

def test_isPrime():
  assert isPrime(2)
  assert isPrime(3)
  assert isPrime(5)
  assert isPrime(7)
  assert not isPrime(4)
  assert not isPrime(105)
  assert not isPrime(333)

def test_nextPrime():
  assert nextPrime(2) == 3
  assert nextPrime(3) == 5
  assert nextPrime(4) == 5
  assert nextPrime(13) == 17
  assert nextPrime(5) == 7
  assert nextPrime(8) == 11


def test_primeFactors():

  primeList1 = [2, 2, 2, 19]
  assert checkListsEqual(primeFactors(2*2*2*19), primeList1)

  primeList2 = [2,2,2,2,5,5,5]
  assert checkListsEqual(primeFactors(2**4 * 5**3), primeList2)

  ############ A More Complex Test ########################

  # generate the next there primes after 1,000
  n = 10**3
  primeList3 = [nextPrime(n), nextPrime(nextPrime(n)), nextPrime(nextPrime(nextPrime(n)))]
  # find their product
  product = np.prod(primeList3)
  assert checkListsEqual(primeFactors(product), primeList3)


def test_fib():
  assert fib(1) == 1
  assert fib(2) == 1
  assert fib(3) == 2
  assert fib(4) == 3
  assert fib(5) == 5
  assert fib(20) == 6765


def test_hanoi():
  moves = hanoi(2)
  movesTrue = ['Move disk 1 from A to B', 'Move disk 2 from A to C', 'Move disk 1 from B to C']
  for move, trueMove in zip(moves, movesTrue):
    assert move == trueMove

  moves = hanoi(3)
  movesTrue = ['Move disk 1 from A to C', 'Move disk 2 from A to B', 'Move disk 1 from C to B',
               'Move disk 3 from A to C', 'Move disk 1 from B to A', 'Move disk 2 from B to C',
               'Move disk 1 from A to C']
  for move, trueMove in zip(moves, movesTrue):
    assert move == trueMove

