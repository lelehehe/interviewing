#region my first implementation, simple and slow
def largestContinuousSum1(a):
    count = len(a)
    max = float('-inf')
    for i in range(count):
        result = 0
        for j in range(i, count):
            result += a[j]
            if result > max:
                max = result
    return max

def test_largestContinuousSum1():
    assert largestContinuousSum1([1,2,-1,3,4,10,10,-10,1]) == 29
    assert largestContinuousSum1([1,2,-1,3,4,10,10,-10,1,-30,25,5,2]) == 32
#endregion