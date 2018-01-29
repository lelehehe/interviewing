# Problem Statement
# Given a list of integers, find the largest product from 3 integers in the list
# example: [-5, -5, 1, 3] returns: -5*-5*3 = 75

import sys

def setPositives(a, i):
    if len(a) < 3:
        a.append(i)
        return
    mini = min(a)
    if (mini > i): 
        return
    print(a)
    for j in range(len(a)):
        if a[j] == mini:
            a[j] = i

def setNegtives(a, i):
    if len(a) < 2: 
        a.append(i)
        return
    maxi = max(a)
    if maxi < i: return
    for j in range(len(a)):
        if a[j] == maxi:
            a[j] = i

def largest_makes(a):
    # get 3 positives
    # get 2 negtivea
    positives = []
    negtives = []

    for i in a:
        setPositives(positives, i)
        if i < 0:
            setNegtives(negtives, i)

    if len(positives) == 3:
        make1 = positives[0] * positives[1] * positives[2]
    else: 
        make1 = float('-inf')
    if len(negtives) == 2:
        make2 = negtives[0] * negtives[1] * max(positives)
    else:
        make2 = float('-inf')
    return max(make1, make2)
    

#endregion

def test_largest_makes():
    stubs = [largest_makes]
    for stub in stubs:    
        assert stub([-5, -5, 1, 3]) == 75
        assert stub([-1, -2, -3, -4]) == -6
        assert stub([1, 2, 3, 4]) == 24
