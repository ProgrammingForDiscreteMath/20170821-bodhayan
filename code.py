# Create a list with the first ten triangular numbers
# (see https://oeis.org/A000217)

L = [i*(i+1)/2 for i in range(10)]

# Create a function to test if a number is prime
def is_prime(n):
    """
    Test if ``n`` is a prime.
    """
    if n<2:
    	return False
    if n==2:
    	return True
    for i in range(2, int(n**0.5)+1):
    	if n%i==0:
    		return False
    return True

# Tests
# is_prime(2033) == False
# is_prime(2039) == True

# Create a function which returns a list of the first ten prime numbers
# greater than or equal to n

def next_ten_primes(n):
    """
    Return the list of the first ten prime numbers greate than or equal to n
    """
    k=10
    i=0
    l=[]
    while k>0:
    	if is_prime(n+i):
    		l.append(n+i)
    		k-=1
    	i+=1
    return l

# Tests
# next_ten_primes(2033) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]
# next_ten_primes(2039) == [2039, 2053, 2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111]






