""" MA3.py

Student:
Mail:
Reviewed by:
Date reviewed:

"""
import random
import matplotlib.pyplot as plt
import math as m
import concurrent.futures as future
from statistics import mean 
from time import perf_counter as pc

def approximate_pi(n): 
    n_c_x= []
    n_c_y = [] 
    n_a_x= []
    n_a_y = []

    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            n_c_x.append(x)
            n_c_y.append(y)
        else:
            n_a_x.append(x)
            n_a_y.append(y)

    plt.figure(figsize=(6,6))
    plt.scatter(n_a_x, n_a_y, s=1, color='blue', label='Outside')
    plt.scatter(n_c_x, n_c_y, s=1, color='red',  label='Inside')
    plt.legend()
    plt.show()       

    return 4 * len(n_c_x) / n  

def sphere_volume(n, d): #Ex2, approximation
    #n is the number of points
    # d is the number of dimensions of the sphere 

    points = map(lambda x: [random.uniform(-1,1) for x in range (d)], range(n))

    inside = map(lambda x: sum(map(lambda s: s*s, x)) <=1 , points) 

    count= sum(inside)


    return (count/n) * (2**d)

def hypersphere_exact(d): #Ex2, real value
    # d is the number of dimensions of the sphere 
    return m.pi **(d/2)/m.gamma(d/2+1)

#Ex3: parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
      #n is the number of points
    # d is the number of dimensions of the sphere
    #np is the number of processes
    with future.ProcessPoolExecutor() as executer:  
         futures = list(executer.submit(sphere_volume, n, d) for i in range (np))
         results = list(f.result() for f in futures)
    return (mean(results))


#Ex4: parallel code - parallelize actual computations by splitting data
# def sphere_volume_parallel2(n,d,np=10):
#     #n is the number of points
#     # d is the number of dimensions of the sphere
#     #np is the number of processes
#      return
    

def sphere_volume_parallel2(n, d, np):
    """
    Parallelize a single Monte Carlo volume computation by splitting n samples
    across np processes, using the existing sphere_volume function for each chunk.
    """
    # Divide n into np chunks (distribute remainder)
    base, rem = divmod(n, np)
    chunks = [base + (1 if i < rem else 0) for i in range(np)]

    with future.ProcessPoolExecutor(max_workers=np) as executor:
        futures = [executor.submit(sphere_volume, p, d) for p in chunks]
        vols = [f.result() for f in futures]
    # Combine via weighted average: each vol_i is for p_i samples
    total_vol = sum(v * p for v, p in zip(vols, chunks))
    return total_vol / n
    
def main():
    # #Ex1
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)
    #Ex2
    n = 100000
    d = 2
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    n = 100000
    d = 11
    sphere_volume(n,d)
    print(f"Actual volume of {d} dimentional sphere = {hypersphere_exact(d)}")

    #Ex3
    n = 100000
    d = 11
    np=10
    time_lista= []
    for y in range (np):
        start = pc()
        y = sphere_volume(n,d)
        end= pc()
        time_lista.append(end-start)
    print(f'Sequential_time={sum(time_lista)}')



    par1_start= pc()
    Parallel_111= sphere_volume_parallel1(n,d,np)
    par1_end= pc()
    print(f'THE PARALLEL_TIME_1= {(par1_end-par1_start)}')
    


    par2_start= pc()
    Parallel_222 =sphere_volume_parallel2(n, d, np)
    par2_end= pc()
    print(f'THE PARALLEL_TIME_2= {(par2_end-par2_start)}')

    
    

if __name__ == '__main__':
	main()
