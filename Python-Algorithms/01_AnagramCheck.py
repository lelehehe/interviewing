#http://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions/Anagram%20Check%20.ipynb
def isAnagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    if len(s1) != len(s2):
        return False
    
    # note: only one dictionary needed to get the job done!!!
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s2:
        if letter in count and count[letter] > 0:
            count[letter] -= 1
        else:
            return False

    return True

def test_isAnagram():
    assert isAnagram('abc', 'bca') == True
    assert isAnagram('clint eastwood', 'olsd west action') == False
    assert isAnagram('clint eastwood', 'old west action') == True