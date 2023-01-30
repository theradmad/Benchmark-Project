import time
import numpy
# Start timer

def benchmark1():
    start_time = time.time()

    for i in range(10**10): 
        6+7
    for i in range(5*10**9): 
        6*7
    for i in range(2*10**9): 
        6/7

# Stop timer
    end_time = time.time()


    execution_time = end_time - start_time
    print("Integer operation benchmark execution time:", execution_time)

#


#read array elements
def benchmark3():

   