from speedsense.tc_estimator import get_time_complexity
def findprimes(x):
    primecount=0
    for i in range(2,x):
        factors=0
        for j in range(2,i):
            if i%j==0:
                factors+=1
        if factors==2:
            primecount+=1
    return primecount
get_time_complexity(findprimes, [10, 15, 20, 25, 30])
