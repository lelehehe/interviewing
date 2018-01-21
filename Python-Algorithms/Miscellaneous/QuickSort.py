# Problem Statement
# .....

#region my implementation
# algorithm is based on 
# https://visualgo.net/en/sorting

def partition(a, lo, hi):
    pivot = a[lo]
    firstBig = hi + 1
    for i in range(lo + 1, hi+1):
        if a[i] > pivot: 
            firstBig = min(firstBig, i)
        elif a[i] < pivot and firstBig < hi + 1: 
            a[firstBig], a[i] = a[i], a[firstBig] #swap
            firstBig += 1
    if firstBig - 1 != lo or firstBig == hi + 1:
        a[lo], a[firstBig - 1] = a[firstBig - 1], a[lo]
        return firstBig - 1
    return lo 
    

def quick_sort(a, lo = 0, hi = -1):
    if hi == -1: hi = len(a) - 1

    if lo < hi:
        print(a)
        # partition it
        par = partition(a, lo, hi)
        print(par)
        quick_sort(a, lo, par - 1)
        quick_sort(a, par + 1, hi)


#endregion

def test_quick_sort():

    a = [3, 1, 4, 2, 6, 5]
    quick_sort(a)
    assert a == [3, 1, 4, 2, 6, 5]
    b = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
    quick_sort(b)
    assert b == [2, 3, 4, 5, 15, 19, 26, 27, 36, 38, 44, 46, 47, 48, 50]

a = [3, 1, 4, 2, 6, 5]
b = [3,44,38,5,47,15,36,26,27,2,46,4,19,50,48]
quick_sort(b)

print(b)