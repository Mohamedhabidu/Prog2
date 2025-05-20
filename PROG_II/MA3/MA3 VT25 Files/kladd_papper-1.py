import random
import matplotlib.pyplot as plt

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

print(approximate_pi(60000))
