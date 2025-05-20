"""
Solutions to module 1
Student: Mohamed Habidu
Mail: mohamed.habidu.3061@student.uu.se
Reviewed by: Anton 
Reviewed date: 4 april 
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make minor 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    """ Ex1: Computes m*n using additions"""
 
    if n == 0: 
        return 0 
    else: 
        return m + multiply(m, (n-1))

    pass


def harmonic(n: int) -> float:              
    """Ex2: Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if n==0: 
     return 0
    else: 
     return (1/n)+harmonic(n-1)

    pass


def get_binary(x: int) -> str:              
    """ Ex3: Returns the binary representation of x """
    if x < 0:
      return '-' + get_binary(-x)
    elif x == 0: 
      return "0"
    elif x== 1: 
      return "1"
    else: 
      return get_binary(x//2) + str(x % 2)


    pass


def reverse_string(s: str) -> str:        
    """Ex4: Returns the s reversed """
    if len(s) <= 1: 
      return s
    else: 
      return  reverse_string(s[1:])+ s[0] 
    pass


def largest(a: iter):                     
    """Ex5: Returns the largest element in a"""
    if len(a) ==1: 
      return a [0]
    mid = len(a)//2
    left_half= largest(a[:mid])
    right_half = largest(a[mid:])

    if left_half > right_half: 
      return left_half
    else: 
      return right_half
    
    pass


def count(x, s: list) -> int:                
    """Ex6: Counts the number of occurences of x on all levels in s"""
    if len(s)==0: 
      return 0
    element_1= s[0]
    total= 0

    if x== element_1: 
      total +=1

    if isinstance(element_1, list):
        total += count(x, element_1)

    total += count(x, s[1:])

    return total 
    pass


def bricklek(f: str, t: str, h: str, n: int) -> str:  
    """Ex7: Returns a string of instruction ow to move the tiles """
    if n == 0: return []
    if n == 1: return [f+'->'+t ]
    return bricklek (f, h, t, n-1)+ [f+'->'+t ]+ bricklek ( h, t,f, n-1)
    pass


def fib(n: int) -> int:                      
    """ For Ex9: Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    








def main():

    times = {}

    for n in [10, 15, 20, 25, 30,35, 40]:
     tstart = time.perf_counter()
     fib(n)
     tstop = time.perf_counter()

    t= tstop -tstart 
    times[n] = t

    print('\nCode that demonstates my implementations\n')

    print('\n\nCode for analysing fib and fib_mem\n')

    print('\nBye!')


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles: 
                #35.7 million years
   
  
  
  Exercise 9: Time for Fibonacci:

                #fib(35) took 2.830 seconds
                #fib(40) took 29.545 seconds

                # x^(40-35)= 29.545/2.830 => x≈ 1.6

                # Time(fib(50)) ≈54 minutes.
                # Time(fib(100)) ≈1.56 million years.
 


  
  
  Exercise 10: Time for fib_mem:

                #value of fib(100)=354224848179261915075
                #time it takes:0.00010606000432744622
  
  
  
  
  
  Exercise 11: Comparison sorting methods:
  
                #Insertion  T= c * n^2, so c = 1/(1000^2)
                # T(1 M)= c* 1M^2= 1M sec = 11.6 days.
                # T(1G) = c* 1G^2= 1T sec = 31,700 years

                #Merge  T = dnlogn , so d= 1/(10^4) 
                # T(1 M) = d* 1 M* log(1M) = 1990 seconds =33.2 minutes
                #T(1G)= d* 1G*log(1G)= 34.6 days.
  
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
                # T(A) = n [s]
                #T(B)= c * n * log(n) [s]
                #Tests show that T(B, n=10)= c * 10* log(10) =1  => c= 1/33 = 0.03

                # Comparison for T(A) < T(B)
                # n < c * n * log(n) 
                # n/(c*n) < log(n)  
                # 33 < log_2(n)

                # n > 2^33
  
"""
