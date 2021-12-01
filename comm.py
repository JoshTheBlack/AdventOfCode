# coding=utf-8
from time import perf_counter
from functools import wraps, reduce,lru_cache
import math

def timed(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        t = end - start
        print(f"{func.__name__}: {t:.6f} seconds or {t*1000:.6f} milliseconds")
        return result
    return wrapper

@lru_cache(maxsize=None)
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def sumDigits(n):
    """Sums the digits in an integer"""
    n = str(n)
    x = 0
    for number in n:
        x += int(number)
    return x

def reverseNumber(num):
    """Takes an integer and returns an integer with the digits reversed"""
    return int(str(num)[::-1])

def isPalindrome(num):
    """Takes an integer and returns true if integer is palindromic."""
    num = str(num)
    if num == num[::-1]: return True
    return False

def sumProperDivisors(num):
    s = set([1])
    for r in range(2, int(num**0.5)+1):
        if num % r == 0:
            s.add(r)
            s.add(num//r)
    return sum(s)

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def orderedFactors(n):
    return [[i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0]
        
def is_prime(n): 
    """ Tests if a number is prime """
    if n <= 1: 
        return False
    if n == 2: 
        return True
    if n > 2 and n % 2 == 0: 
        return False
    max_div = math.floor(math.sqrt(n)) 
    for i in range(3, 1 + max_div, 2): 
        if n % i == 0: 
            return False
    return True

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

def rotateDigits(n):
    """ Creates a set of all possible rotations of an integer.  i.e. 123 returns (123, 231, 312)"""
    rotations = set()
    for i in range( len( str(n) ) ):
        rotations.add(int( str(n)[i:] + str(n)[:i] ))
    return rotations

def primeSieveRange(*args):
    """ Returns  a list of primes between 'start' (inclusive) and 'end' (exclusive) 
    
        Takes 1 or 2 arguments.  If 1 argument is passed, it is the 'end' value.
        If 2 arguments are passed, they are (start, end)"""
    if len(args) > 2:
        raise Exception("Too many arguments")
    elif len(args) == 2:
        start, end = args[0], args[1]
    elif len(args) == 1:
        start, end = 0, args[0]
    else:
        start,end = 0, 10
    add2 = False
    sieve = [True] * end
    if start < 3:
        start, add2 = 3, True
    elif start % 2 == 0:
        start += 1
    for i in range(3,int(end**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((end-i*i-1)//(2*i)+1)
    if add2 == True:
        return [2] + [i for i in range(3,end,2) if sieve[i]]
    return [i for i in range(start,end,2) if sieve[i]]

def checkPandigital(number):
    digits = []
    length = len(str(number))
    for letter in str(number):
        digits.append(int(letter))
    if set(digits) == set(range(1,length+1)):
        return True
    else:
        return False

def isTri(x):
    y = ((8*x+1)**0.5-1)/2
    if y - int(y) == 0:
        return True, int(y)
    else:
        return False, 0

def isPent(x):
    y = (((24 * x) + 1)**0.5 + 1) / 6
    if y - int(y) == 0:
        return True, int(y)
    else:
        return False, 0

def isHex(x):
    y = ((8*x+1)**0.5+1)/4
    if y - int(y) == 0:
        return True, int(y)
    else: 
        return False, 0

def isHept(x):
    y = ((40*x + 9)**0.5 + 3)/10
    if y - int(y) == 0:
        return True, int(y)
    return False, 0

def isOct(x):
    y = ((48*x+16)**0.5+4)/12
    if y - int(y) == 0: return True, int(y)
    return False, 0

def generateFactors(num,values,factors):
    if len(values[num]) > 0:
        factors += values[num]
        return factors
    else:
        for i in range(2,num-1):
            if num % i == 0:
                return generateFactors(num//i,values,factors+[i])

def convertToAscii(data):
    ###Takes in a list of ASCII codes and returns a string###
    result = ""
    for bit in data:
        result += chr(bit)
    return result

def partition(items, total):
    '''Returns the number of ways that {total} can be summed to using values in the array {items}'''
    table = [0 for i in range(total+1)] 
    table[0] = 1
    for i in range(0,len(items)): 
        for j in range(items[i],total+1): 
            table[j] += table[j-items[i]] 
    return table[total]