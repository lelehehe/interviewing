# https://www.geeksforgeeks.org/lexicographic-rank-string-duplicate-characters/

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
import math

def inSortedLoc(s, c):
    for i in range(len(s)):
        if c == s[i]: return i
    return -1

def lexico_rank(s):
    rank = 1
    s_sorted = "".join(sorted(s))
    print("old:{} new:{}".format(s, s_sorted))

    # coding sample: ginrst -> string
    for i in range(len(s)):
        if s[i] == s_sorted[i]: pass
        # diff s vs g
        j = inSortedLoc(s_sorted, s[i])
        # loop g, i, n r before s
        extra = j * math.factorial(len(s) - i - 1)
        rank += extra
        print("j: {} diff: {} factorial: {} extra: {}, rank: {}".format(j, len(s) - j, len(s) - i - 1, extra, rank))

    return rank

#endregion

def test_lexico_rank():
    stubs = [lexico_rank]
    for stub in stubs:    
        assert stub('acb') == 2
        assert stub('string') == 598
        assert stub('cba') == 6
        assert stub('settLe') == 107
        assert stub('abab') == 2
        assert stub('') == 2

lexico_rank('string')