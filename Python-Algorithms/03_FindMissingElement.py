#region my first implementation
def dictionaryItemPlusOne(a, i):
    if i in a:
        a[i] += 1
    else:
        a[i] = 1

def dictionaryItemMinusOne(a, i):
    if i in a:
        a[i] -= 1
    else:
        a[i] = 1

def finder(a1, a2):
    helper = {}
    for i in a1:
        dictionaryItemPlusOne(helper, i)
    for i in a2:
        helper[i] -= 1

    for key, value in helper.items():
        if value == 1:
            return key
def test_finder():
    assert finder([1,2,3,4,5,6], [6,4,2,3,1]) == 5
    assert finder([2], []) == 2
    assert finder([5, 5, 7, 7], [7, 5, 7]) == 5
#endregion

#region better version:
# 1. aim to the 2nd dict and if found the extra item in first dict, early stop!!!
# 2. use defaultdict
import collections

def finder2(a1, a2):
    d = collections.defaultdict(int)

    for i in a2:
        d[i] += 1

    for i in a1:
        if d[i] == 0:
            return i
        else: 
            d[i] -= 1

def test_finder2():
    assert finder2([1,2,3,4,5,6], [6,4,2,3,1]) == 5
    assert finder2([2], []) == 2
    assert finder2([5, 5, 7, 7], [7, 5, 7]) == 5

finder2([1,2,3,4,5,6], [6,4,2,3,1])
#endregion

#region XOR version
#this is the best one using XOR
def finderXOR(a1, a2):
    result = 0
    for i in (a1 + a2):
        result ^= i
    
    return result

def test_finderXOR():
    assert finderXOR([1,2,3,4,5,6], [6,4,2,3,1]) == 5
    assert finderXOR([2], []) == 2
    assert finderXOR([5, 5, 7, 7], [7, 5, 7]) == 5
#endregion