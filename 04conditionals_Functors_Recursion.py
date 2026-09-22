""" Connditionals 
@author: Patrick
"""

###### If elif and else
# x = int(input("Give me a number:"))
x = 0
if x < 5:
    print("too low!")
elif x > 9:
    print("too high!")
else:
    print("That should be enough")
print("done")
# One flow: True
# Another:  False, True
# Another:  False, False
# Exactly 3 possibilities! No more, no less

###### more Execution flow
aList = [5, 3, 7, 2, 2]
if 7 in aList:
    print("found magic number!")
if 7 not in aList:
    print("no magic number!")
# One flow: False, False, 
# Another:  False, True
# Another:  True , False
# Another:  True , True
#### The number of flows != number of ifs! 
## more ifs generally means the more tests are needed...


import sys; sys.exit()


###### The 'switch' in java
''' // In Java programming language: 
int xTheVerySpecialNumber = 53
switch(xTheVerySpecialNumber) {
    case 24:
    case 42:
        System.out.println("42 is the best!");
        break;
    case 75:
        System.out.println("Found 75!");
        break;
    default:
        System.out.println("Just a normal number");
        break;
}
'''

###### Python doesn't have switch, but it can do a switcher
# x = int(input("Input number for switcher:"))
xSwitcher = {
    42: "42 is very awesome", 
    13: "13 is unlucky",
    91: "91 is a perfect square"
    }
x = 42
print(xSwitcher.get(x, "default case?"))
print(xSwitcher.get(91, "Just a normal number"))


###### More complex actions means use a function-switcher
def num42():
    print("42 is a special number")
    print("It is the answer to life")

def num13():
    print("13 is unlucky")
    print("You should use 14 instead")

def num121():
    print("121 is a perfect square already")

def normNumber():
    print("That's just a normal number")

xSwitcher = {
    42: num42,
    -42: num42,
    13: num13,
    91: num121
    }
print("Using function switcher:")
userInput = getUserInput()
selectedFunctor = xSwitcher.get(userInput, normNumber)
selectedFunctor()
print(xSwitcher.get(37, normNumber)())




###### Recursion: the good and bad
print("Recursion Now!")

def factorial(x):
    ### Base case should always be checked FIRST
    if x == 1:
        return 1
    ### Recursive case:
    return x * factorial(x-1)

print("Some Algorithms take longer than others") 
print("even if they work with smaller numbers")

prod = 1
for i in range(1, 31):
    prod = prod* i
print("prod = ", prod)


num = 30
print(f"factorial({num}) = {factorial(num)}") # some f-strings here too

def fibonnaci(x):
    if x < 2:
        return x
    # multi-recursive function calls! :
    return fibonnaci(x-1) + fibonnaci(x-2)

print(f"{fibonnaci(num)= }")
print(fibonnaci(30))


def qSort(itemsList):
    if len(itemsList) == 0: return []
    mid = len(itemsList) // 2
    leftSide = itemsList[:mid]
    rightSide = itemsList[mid:]
    return combine(qSort(leftSide, qSort(rightSide)))


def combine(left, right):
    result = []
    leftI, rightI = 0 , 0
    while(leftI < len(left) and rightI < len(right)):
        if (left[leftI] < right[rightI]):
            result.append(left[leftI])
            leftI += 1
        else: 
            result.append(right[rightI])
            rightI += 1
    for thisI in range(leftI, len(left)):
        result.append(left[thisI])
    for thisI in range(rightI, len(right)):
        result.append(right[thisI])
    return result


def otherSort(aList):
    pass

def otherSort2(aList):
    pass

for functionTotest in [qSort, otherSort, otherSort2]:
    assert functionTotest([5, 3, 7, 2, 2]) == [2, 2, 3, 5, 7]
    assert functionTotest([]) == []
    assert functionTotest([1]) == [1]
    assert functionTotest([1, 2]) == [1, 2]


print(sorted("zxywabc"))




import sys; sys.exit()

import time
startTime = time.time()
sumEvens=list(range(0, 10000000, 2))
duration = time.time() - startTime
print(f"Time taken: {duration} seconds")


for func in [sum, sumEvens]:
    startTime = time.time()
    result = func(list(range(0, 10000000, 2)))
    duration = time.time() - startTime
    print(f"Time taken: {duration} seconds")




def someSort(aList):
    breakpoint()
    return sorted(aList)


def funnySort(aList):
    for i in range(len(aList)):
        for j in range(len(aList)):
            if aList[i] < aList[j]:
                aList[i], aList[j] = aList[j], aList[i]
    return aList



# HA DADO EN CLASE EL DEBUGER POR TERMIANL 