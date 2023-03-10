import time
import numpy
# Start timer

# f = open('bench_file1.txt', 'x')

# z = open('bench_file2.txt', 'x')

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
    
    arr1 = [0]*10**9
    
    
    for i in range(10**9):
        
        v = arr1[i]
        
        arr1[i]=1
    for i in range(10**9):
        
        v = arr1[i]
        
        arr1[i]=1
    for i in range(10**9):
        
        v = arr1[i]
        
        arr1[i]=1
    for i in range(10**9):
        
        v = arr1[i]
        
        arr1[i]=1
    for i in range(10**9):
        
        v = arr1[i]
        
        arr1[i]=1
        
    end_time = time.time()

    execution_time = end_time - start_time
    print("Array operation benchmark execution time:", execution_time)

def benchmark4():  
    start = time.time()
    with open('bench_file1.txt','wb') as f:
        for i in range(10**9):
            f.write(b'0'*100)
    with open('bench_file1.txt','rb') as f:
        for i in range(10**9):
            l = f.read(100)
    end = time.time()

    execution_time = end - start
    print("Hard drive benchmark 1 execution time:", execution_time)

def benchmark5():  
    start = time.time()
    with open('bench_file2.txt','wb') as f:
        for i in range(10**9):
            f.write(b'0'*10000)
    with open('bench_file2.txt','rb') as f:
        for i in range(10**5):
            l = f.read(10000)
    end = time.time()

    execution_time = end - start
    print("Hard drive benchmark 2 execution time:", execution_time)











    
       
