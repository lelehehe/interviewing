# https://www.geeksforgeeks.org/trapping-rain-water/

# Given n non-negative integers representing an elevation map where the width of each bar is 1, 
# compute how much water it is able to trap after raining.

# Input: arr[]   = {2, 0, 2}
# Output: 2
# Structure is like below
# | |
# |_|
# We can trap 2 units of water in the middle gap.

# Input: arr[]   = {3, 0, 0, 2, 0, 4}
# Output: 10
# Structure is like below
#      |
# |    |
# |  | |
# |__|_| 
# We can trap "3*2 units" of water between 3 an 2,
# "1 unit" on top of bar 2 and "3 units" between 2 
# and 4.  See below diagram also.

# Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# Output: 6
#        | 
#    |   || |
# _|_||_||||||
# Trap "1 unit" between first 1 and 2, "4 units" between

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
def TrappingWater(bars):
    left = [0] * len(bars)
    right = [0] * len(bars)

    left[0] = bars[0]
    for i in range(1, len(bars)):
        left[i] = max(left[i - 1], bars[i])
    right[::-1] = bars[::-1]
    for i in range(len(bars)-2, 0, -1):
        right[i] = max(right[i + 1], bars[i])

    result = 0
    for i in range(len(bars)):
        result += min(left[i], right[i]) - bars[i]
    
    return result

#endregion

def test_TrappingWater():
    stubs = [TrappingWater]
    for stub in stubs:    
        assert stub([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
        assert stub([3, 0, 0, 2, 0, 4]) == 10
