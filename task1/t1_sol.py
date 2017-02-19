

def quad(a,b,c,x):
  return a*x**2+b*x+c

def quadIsZero(a,b,c,x):
  return quad(a,b,c,x) == 0


print(quad(1,2,0,1))
print(quad(1,0,0,1))


print(quadIsZero(1,2,0,1))
print(quadIsZero(1,0,-1,1))
