""" Some examples using list comprehensions and basic timing of functions. 
@author: Patrick
"""

def sumEvens(aList):
    evensList = []
    for n in aList:
        if n % 2 == 0:
            evensList.append(n)
    return sum(evensList)
    
def sumEvensComp(aList):
    evensList = [n for n in aList if n % 2 == 0]
    return sum(evensList)

def sumEvensCounter(aList):
    numsSum = 0
    for n in aList:
        if n % 2 == 0:
            numsSum += n
    return numsSum


import time # python module used for tracking/calculating time

start = time.time()
sumEvensCounter(list(range(33, 4600000, 5)))
duration = time.time() - start
print("count style:    ", duration)

start = time.time()
sumEvens(list(range(33, 4600000, 5)))
duration = time.time() - start
print("basic list style", duration)

start = time.time()
sumEvensComp(list(range(33, 4600000, 5)))
duration = time.time() - start
print("list comp style ", duration)

# hmmm that's a lot of very similar-looking code.  
# is there a better way to do this?  YES

funcsAndTitles = [(sumEvens, "sumEvens"), 
                  (sumEvensComp, "sumEvensComp"), 
                  (sumEvensCounter, "sumEvensCounter")]
# ^^^ one list, but each item can be "unpacked" into two things:

for theFunc, theTitle in funcsAndTitles:
    start = time.time()
    theFunc(list(range(33, 4600000, 5)))
    duration = time.time() - start
    print(f"  {theTitle} time = ", duration)


# is there an even better way to identify each function by __name__?
# and what about about making the timing part of a function?
# ....  YES WE CAN!


for theFunc in [sumEvens, sumEvensComp, sumEvensCounter]:
    # print("testing for function: ", theFunc.__name__)
    start = time.time()
    theFunc(list(range(33, 4600000, 5)))
    duration = time.time() - start
    print(f"{theFunc.__name__} took {duration} time")

a = 2
b = 7
c = a ** b ** a
c -= 1553295


import sys; sys.exit()


# how does it hold for random numbers?
import random
aRandDecimal =  random()
aRandInt = random.randint(3, 44)


