# Given:
#   'abcade'
# Return:
#   False

#region my implementation
def uniqueChar(s):
    dict = {}
    for c in s:
        if c in dict:
            return False
        else:
            dict[c] = True
    return True

# use set is better than dict
def uniqueCharUseSet(s):
    chars = set()
    for c in s:
        if c in chars:
            return False
        else:
            chars.add(c)
    return True
#endregion

def test_uniqueChar():
    stubs = [uniqueChar, uniqueCharUseSet]
    for stub in stubs:    
        assert stub('abcade') == False
        assert stub('') == True
        assert stub('a') == True
        assert stub('abc def') == True
