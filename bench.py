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

    arr1 = np.array[None]*10**9
    arr2 = np.array[None]*10**9
    arr3 = np.array[None]*10**9
    arr5 = np.array[None]*10**9
    arr4 = np.array[None]*10**9
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
    
