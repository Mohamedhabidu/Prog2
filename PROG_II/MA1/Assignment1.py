
import math 
# EX 1

def multiply(m, n): 
    if n == 0: 
        return 0 
    else: 
        return m + multiply(m, n-1)


#print (multiply(10, 5))

#Ex2
def harmonic(n): 
    if n==0: 
     return 0
    else: 
     return (1/n)+harmonic(n-1)


#print(harmonic(2))

#Ex3

def get_binary(x):
   if x < 0:
      return '-' + get_binary(-x)
   elif x == 0: 
      return "0"
   elif x== 1: 
      return "1"
   else: 
      return get_binary(x//2) + str(x % 2)


#print(get_binary(-18))

#Ex4


def reverse_string(s): 
   if len(s) <= 1: 
      return s
   else: 
      return  reverse_string(s[1:])+ s[0] 

#print(reverse_string("hello"))




 
def reverse_string(x):
    if len(x) <= 1:
        return x
    else:
        mid = len(x)//2
        return reverse_string(x[mid:]) + reverse_string(x[:mid])


    
#print(reverse_string("hello"))
   
##Ex5

def largest(a): 
   if len(a) ==1: 
      return a [0]
   mid = len(a)//2
   left_half= largest(a[:mid])
   right_half = largest(a[mid:])

   if left_half > right_half: 
      return left_half
   else: 
      return right_half
   

#print (largest([10, 2, 3, 4, 8, 50, 7, 8,9 ,1, 4]))



# Ex6 

def count_top(x, s): 
   if len(s)==0: 
      return 0
   if x == s[0]:
      i = 1 
   else:
      i= 0 
 
   return i+ count_top(x, s[1:])

#print(count_top(4, [1, 4, 2, ['a', [[4], 3, 4]]]))

def count_all(x, s): 
   if len(s)==0: 
      return 0
   element_1= s[0]
   total= 0

   if x== element_1: 
      total +=1

   if isinstance(element_1, list):
        total += count_all(x, element_1)

   total += count_all(x, s[1:])

   return total 

#print(count_all(4, [1, 4, 2, ['a', [[4], 3, 4]]]))


#EX7

def bricklek (f, t, h, n): 
   if n == 0: return []
   if n == 1: return [f+'->'+t ]
   return bricklek (f, h, t, n-1)+ [f+'->'+t ]+ bricklek ( h, t,f, n-1)
   
print(bricklek('f', 't', 'h', 3))



#Ex8 35.7 million years


#Ex9 



import time


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    


times = {}

for n in [10, 15, 20, 25, 30,35, 40]:
    tstart = time.perf_counter()
    fib(n)

    tstop = time.perf_counter()


    t= tstop -tstart 
    times[n] = t
print(f"fib({n}) took {t} seconds")

#fib(35) took 2.83040049700503 seconds
#fib(40) took 29.54531770200265 seconds

# x^(40-35)= 29.545/2.830 => x≈ 1.6

# Time(fib(50)) ≈54 minutes. 
# Time(fib(100)) ≈1.56 million years.

#Ex10

import time

memory = {0:0, 1:1}
def fib_mem(n):
    if n not in memory:
        memory[n] = fib_mem(n-1) + fib_mem(n-2)
    return memory[n]

tstart_m = time.perf_counter()
V= fib_mem(100) 
tstop_m = time.perf_counter()
t_m= tstop_m-tstart_m

print(f'value of fib(100)={V}')
print (f'time it takes:{t_m}' )



#Ex 11

#Insertion  T= c * n^2, so c = 1/(1000^2)
# T(1 M)= c* 1M^2= 1M sec = 11.6 days.
# T(1G) = c* 1G^2= 1T sec = 31,700 years

#Merge  T = dnlogn , so d= 1/(10^4) 
# T(1 M) = d* 1 M* log(1M) = 1990 seconds =33.2 minutes
#T(1G)= d* 1G*log(1G)= 34.6 days.




#EX 12

# T(A) = n [s]
#T(B)= c * n * log(n) [s]
#Tests show that T(B, n=10)= c * 10* log(10) =1  => c= 1/33 = 0.03

# Comparison for T(A) < T(B)
# n < c * n * log(n) 
# n/(c*n) < log(n)  
# 33 < log_2(n)

# n > 2^33