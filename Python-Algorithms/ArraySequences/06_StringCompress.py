# Given:
#   'AAABCCCaaYYY'
# Return:
#   'A3B1C3a2Y3'

#region my implementation
def stringCompress(s):
    data = []
    current = ''
    count = 0
    for i in range(0, len(s)):
        if s[i] == current and i != len(s) - 1:
            count += 1
        elif s[i] != current or (i == len(s) - 1):
            if i == len(s) - 1: 
                count += 1
            if current != '': #save item first
                data.append("{}{}".format(current,count))
            count = 1
            current = s[i]
    
    return ''.join(data)
#endregion

def test_stringCompress():
    stubs = [stringCompress]
    for stub in stubs:    
        assert stub('AAABCCCaaYYY') == 'A3B1C3a2Y3'
        assert stub('') == ''
        assert stub('AABBCC') == 'A2B2C2'
        assert stub('AAABCCDDDDD') == 'A3B1C2D5'
