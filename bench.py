import time
import numpy
# Start timer

f = open('bench_file1.txt', 'x')

z = open('bench_file2.txt', 'x')

def benchmark1(): #reference time = 100s
    start_time = time.time()

    for i in range(10**10): 
        6+7
    for i in range(5*10**9): 
        6*7
    for i in range(2*10**9): 
        6/7

    end_time = time.time()

    execution_time = end_time - start_time
    print("Integer operation benchmark execution time:", execution_time)


def benchmark2():
    start_time = time.time()

    for i in range(10**10): 
        6.01+7.01
    for i in range(5*10**9): 
        6.23*7.45
    for i in range(2*10**9): 
        6.98/7.45

    end_time = time.time()

    execution_time = end_time - start_time
    print("Floating point operation benchmark execution time:", execution_time)


#read array elements
def benchmark3():
    start_time= time.time()
    arr1 = [None]*10**9
    arr2 = [None]*10**9
    arr3 = [None]*10**9
    arr5 = [None]*10**9
    arr4 = [None]*10**9
    for i in range(len(arr1)):
        v = arr1[i]
        w = arr2[i]
        x = arr3[i]
        y = arr4[i]
        z = arr5[i]
        arr1[i]=1
        arr2[i]=1
        arr3[i]=1
        arr4[i]=1
        arr5[i]=1
    end_time = time.time()

    execution_time = end_time - start_time
    print("Array operation benchmark execution time:", execution_time)










    
       