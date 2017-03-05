import math
def quad(a,b,c,x):
    ''' (float,float,float,int)-> int

    Using three floats a,b,c as input, returns the value of the quadratic
    function f(x)=axx+bx+c.
    
    >>> quad(1,2,0,1)
    3
    >>> quad(1,0,0,1)
    1
    >>> quad(0,4,-2,1)
    2
    >>>quad(1,2,4,1)
    7
    '''
    f=a*x*x+b*x+c
    return f

def quadIsZero(a,b,c,x):
    '''
    (float,float,float,int)->bool

    Using as arguments a,b,c and x,returns True if and only if the
    quadratic expression evaluates to 0,otherwise False.
    
    >>> quadIsZero(1,2,0,1)
    False
    >>> quadIsZero(1,0,-1,1)
    True
    >>> quadIsZero(0,0,-5,5)
    False
    '''
    variable=False
    if quad(a,b,c,x)==0:
        variable=True
    else:
        variable=False
    return variable

def quadSolver(a,b,c):
    ''' (float,float,float,int)->float

    Using a,b,c,x as arguments, returns the two roots of a quadratic equation.
    
    >>> quadSolver(1,2,0)
    (0.0, -2.0)
    >>> quadSolver(1,2,4)
    None
    >>> quadSolver(-2,-5,4)
    (-3.13745, 0.63745)
  
    '''
    
    
    
    if math.sqrt(b*b-4*a*c)>=0:
        x1=(-b+math.sqrt(b*b-4*a*c))/2*a
        print(x1)
        x2=(-b-math.sqrt(b*b-4*a*c))/2*a
        print(x2)
        return (x1,x2) 
    elif math.sqrt(b*b-4*a*c)<0:
        print(x1,x2)
        return None

def toUpperCase(sentence):       
    ''' (str)->str

    Returns a string containing the letters at the beginning of every word
    to uppercase.
    
    toUpperCase('ana are mere si pere')
    'Ana Are Mere Si Pere'
    toUpperCase('robert invata repede informatica')
    'Robert Invata Repede Informatica'
    '''
    isAtBegWord=True
    s=''

    for char in sentence:
      d = char
      if isAtBegWord == True:
        d = char.upper()
      if char == ' ':
        isAtBegWord == True
      else:
        isAtBegWord == False

      s = s + d
    return s


def toUpperCase2(sentence):
    ''' (str)->str

    Returns a string containing the letters at the beginning of every word
    to uppercase.
    
    toUpperCase2('ana are mere si pere')
    'Ana Are Mere Si Pere'
    toUpperCase2('robert invata repede informatica')
    'Robert Invata Repede Informatica'
    '''
##    s=sentence.title()
##    return s
    s=''
    print(sentence)
    print(sentence.split())
    list=[word[0].upper()+word[1:] for word in sentence.split()]
    print(list)
    s=' '.join(list)
    return s

print(toUpperCase2('ana are mere si pere'))
# print(adsa)


def isPrime(n):
    ''' (int)->bool

    Returns true if and only if an int n is prime, else False.

    Precondition: n>=2
    
    >>> isPrime(2)
    True
    >>> isPrime(4)
    False
    '''
    
    return n>1 and all(n%i for i in range(2,n))

print(isPrime(2))
print(isPrime(3))
print(isPrime(5))
print(isPrime(10))
print(isPrime(15))
print(adsad)

def nextPrime(n):
    ''' (int)->int

    Return the smallest prime number after a given number n.
    
    >>> nextPrime(2)
    3
    >>> nextPrime(3)
    5
    >>> nextPrime(4)
    5
    >>> nextPrime(13)
    17
    >>> nextPrime(5)
    7
    >>> nextPrime(8)
    11
    '''
    
    m=n+3
    for i in range(2,n):
        if n%i!=0:
            for j in range(n+1,m):
                if m%j!=0:
                    return m
    return m
