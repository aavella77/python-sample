 Fibonacci Series
# F(x) = F(x-1) + F(x-2)
# e.g. [0, 1, 1, 2, 3, 5, 8, ....]
# White a function to return ith in Fibonacci series
# 1: 0, 4: 2, ...

def fibonacci(i):
    if (i == 1):
        return 0
    if (i == 2):
        return 1
    fx = fibonacci(i-1) + fibonacii(i-2)
    return fx
    

fibonacci(3) 

def fibonacci2(i):

    fx = []
    if (i == 1):
        return 0
    if (i == 2):
        return 1    
    fx.append(0)
    fx.append(1)
    for j in range(i):
        fx.append(fx[j] + fx[j+1])
    return fx[i-1]         
            
fibonnaci2(3)

0, 1, 2
0: fx = [0, 1, 1]
1: fx = [0, 1, 1, 2]
2: fx = [0, 1, 1, 2, 3]

return fx[2] = 1
            

