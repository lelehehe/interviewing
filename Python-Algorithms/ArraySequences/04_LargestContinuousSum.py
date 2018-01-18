#http://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions%20-%20SOLUTIONS/Largest%20Continuous%20Sum%20-%20SOLUTION.ipynb
#region my first implementation, simple and slow
def largestContinuousSum1(a):
    if len(a) == 0:
        return 0
    count = len(a)
    max = float('-inf')
    for i in range(count):
        result = 0
        for j in range(i, count):
            result += a[j]
            if result > max:
                max = result
    return max
#endregion
#region right answer, local sum is the key
def largestContinuousSum2(a):
    if len(a) == 0:
        return 0
    if len(a) == 1:
        return a[0]
    result = float('-inf')
    past = float('-inf')
    for i in a:
        past = max(past, 0) + i
        result = max(past, result)
        
    return result
#endregion

def test_largestContinuousSum():
    stubs = [largestContinuousSum1, largestContinuousSum2, largestContinuousSum3]
    for stub in stubs:
        assert stub([1,2,-1,3,4,10,10,-10,1]) == 29
        assert stub([1,2,-1,3,4,10,10,-10,1,-30,25,5,2]) == 32
        assert stub([1,2,-1,3,4,-1]) == 9
        assert stub([1,-1]) == 1
        assert stub([]) == 0
        assert stub([-5]) == -5

