''' A showcase of ways of doing the starOut() function. 
We can also time them to see how different code affects 
efficiency to solve larger problems. Some efficiencies are not obvious!
author: Patrick Sullivan
'''

from time import time
import sys
smallProbs = 10_0000
tStr = "sev***e*ral s**tars across the  * universee*" # the test string
answerStr = "seal ars across the universe"

bigProbSize = int(len(tStr) * smallProbs)
bigTStr = tStr * int(bigProbSize // len(tStr))

print(f"     Time to solve a size={len(tStr)} problem {smallProbs} times")
print(f"      |         Time to solve a size={bigProbSize} problem once")
print(f"      V           V")

def testStarOutTimed(soFunc, info="No description"):
    ''' This is a utility function for testing and measuring starOut functions'''
    smallDur, bigDur = "ERROR", "ERROR"
    errors = []
    try:
        start = time()
        for _ in range(smallProbs):
            # call our function on MANY small input strings
            s = soFunc(tStr)
        end = time()
        assert s == answerStr, f"input={tStr}   result={s}"
        smallDur = int(1000*(end - start))
    except Exception as e:
        errors.append(e)
    try:
        start = time()
        result = soFunc(bigTStr) # One BIG input string
        end = time()
        bigDur = int(1000*(end - start))
    except Exception as e:
        errors.append(e)
    print(f"Took {smallDur:<5} ms and {bigDur:<5} ms: info={info}")
    # ^^ another cool f-string moment: can nicely align output!
    if errors:
        print("                    Errors are:", errors)


def starOut(aString): #Solid, readable, reduced-ifs solution.  Nice enumerate
    result = ''
    for i, ch in enumerate(aString):
        if i > 0 and aString[i-1] == '*':
            pass
        elif i+1 < len(aString) and aString[i+1] == '*':
            pass
        elif ch != '*':
            result += ch
    return result
testStarOutTimed(starOut, "simple direct ifs with enumerate")

# print("Exiting early for demo purposes..."), sys.exit(0) # stops program EARLY

def starOut(aString): ### "YOU MUST CONSTRUCT ADDITIONAL PYLO- I mean IFs!"
    result = ''
    sLen = len(aString)
    for i in range(sLen):
        ch = aString[i]
        if i == 0:
            if i+1 < sLen:
                if ch != '*':
                    if aString[i+1] != '*':
                        result += ch
        if i+1 == sLen:
            if i > 0:
                if ch != '*':
                    if aString[i-1] != '*':
                        result += ch
        if i > 0:
            if i < sLen-1:
                if aString[i-1] != '*':
                    if aString[i+1] != '*':
                        if ch != '*':
                            result += ch
    return result
testStarOutTimed(starOut, "many many basic ifs")


def starOut(aString): # a fast, few-comparison, low-level solution using a counter
    counter = -2 if aString[0] == '*' else 0
    result = [] # use a list, since list.append is faster than str+str
    for i in range(1, len(aString)):
        if aString[i] == '*':
            counter = -3
        counter += 1
        if counter > 0:
            result.append(aString[i-1])
    if counter > 0:
        result.append(aString[-1])
    return ''.join(result)
testStarOutTimed(starOut, "fast counter")

def starOut(aString): # slicing-triple-search solution
    aString = ' ' + aString + ' '
    res = ''
    for i in range(1, len(aString)-1):
        if '*' not in aString[i-1:i+2]:
            res += aString[i]
    return res
testStarOutTimed(starOut, "slicing-triple-search")

def starOut(aString): # cool solution that uses shifts and groups them using zip
    shift1 = ' ' + aString[:-1]
    shift2 = aString[1:] + ' '
    result = ''
    for chars in zip(shift1, aString, shift2):
        if '*' not in chars:
            result += chars[1]
    return result
testStarOutTimed(starOut, "shifted-groups-zip")

def starOut(aString):  # Fast and Elegant solution using split and slicing!
    aString = ' ' + aString + ' '
    splits = aString.split('*')
    splitsMinusEnds = [s[1:-1] for s in splits]
    return ''.join(splitsMinusEnds)
testStarOutTimed(starOut, "Elegant split-slicing")

def starOut(aString): # I call this the 'boolean list sweeper'
    blns = [c == '*' for c in aString]
    for i in range(0, len(aString)-1):
        blns[i] = blns[i] or blns[i+1]
    for i in range(len(aString)-1, 1, -1):
        blns[i] = blns[i] or blns[i-1]
    chars = [c for c, b in zip(aString, blns) if not b]
    return ''.join(chars)
testStarOutTimed(starOut, "boolean list sweeper")

def starOut(aString): # RECURSION! No loops. So elegant. Too bad it's VERY slow
    if '*' not in aString:
        return aString
    elif len(aString) > 1 and aString[1] == '*':
        return starOut(aString[1:])
    elif aString[0] == '*':
        return starOut(aString[2:])
    else:
        return aString[0] + starOut(aString[1:])    
testStarOutTimed(starOut, "Recursion, no-loops, single-char, SLOW")
# ^^^ Warning: MemoryError or RecursionError will happen on large input strings!

def starOut(aString): # RECURSION! But faster, group slicing
    while '**' in aString:
        aString = aString.replace("**", "*")
    def starRecur(aString):
        if len(aString) == 0: return ""
        starIndex = aString.find('*')
        if starIndex == -1:
            return aString
        elif starIndex < 2:
            return starRecur(aString[starIndex+2:])
        else:
            return aString[:starIndex-1] + starRecur(aString[starIndex+2:])
    return starRecur(aString)
testStarOutTimed(starOut, "Recursion, slicing, SLOW")
# ^^^ Warning: MemoryError or RecursionError will happen on large input strings!


def starOut(aString): # Divide-and-conquer Recursion! 
    while '**' in aString:
        aString = aString.replace("**", "*")
    def starRecur(aString):
        mid = len(aString) // 2
        midStar = max(aString.find('*', mid), aString.rfind('*', 0, mid))
        if midStar == -1:
            return aString
        return starRecur(aString[:midStar-1]) + starRecur(aString[midStar+2:])
    return starRecur(aString)
testStarOutTimed(starOut, "Recursion Divide-and-Conquer")
# ^^^ Works fine on large input strings... huh!


import re # The POWER of Regular Expressions!
#  See https://regex101.com/r/KdqH1H/2

def starOut(aString):
    re.purge() # just clears the cache, to better test actual efficiency
    return re.sub(r'.?\*+.?', '', aString) 
    # ^^ replace any characters next to a group of stars with nothing!
testStarOutTimed(starOut, "REGEX simple")

rePattern = re.compile(r'.?\*+.?')
def starOut(aString): # Regex, but now pattern is compiled and saved just once
    return rePattern.sub('', aString)
testStarOutTimed(starOut, "REGEX compiled")

def starOut(aString): ## This is just ... dumb
    return ''.join([ch[1] for ch in zip(' ' + aString[:-1], aString, aString[1:] + ' ') if '*' not in ch])
testStarOutTimed(starOut, "one-liner of shifted-zip")

def starOut(aString): # Somehow, an even more terrible one-liner:
    return ''.join([ch for i, ch in enumerate(aString) if ch != '*' and (i <= 0 or aString[i-1] != '*') and (i+1 >= len(aString) or aString[i+1] != '*')])
testStarOutTimed(starOut, "one-liner of enumerated-complex-ifs")

def starOut(aString): # A split-sliciing  one-liner... meh
    return ''.join([s[1:-1] for s in (' ' + aString + ' ').split('*')])
testStarOutTimed(starOut, "one-liner of split-slicer")

print("all done")

# Still curious about more?  
# See the itertools module in python, it is just an import away
#  Interested in more precise perfomance timing?  See the timeit module
