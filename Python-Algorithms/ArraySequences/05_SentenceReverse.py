# reverse all the words in sentence.
# Given:
#   'This is the best'
# Return:
#   'best the is This'

#region my implementation
def sentenceReverse0(s):
    return " ".join(reversed(s.split()))

def sentenceReverse(s):
    #1 get words from sentence
    words = []
    start = -1
    end = 0
    found = False
    for i in range(0, len(s)):
        if not found: 
            if s[i] == ' ':
                pass
            else: 
                found = True
                start = i
        else: 
            if s[i] == ' ' or i == len(s) - 1:  # found a word
                if i == len(s) - 1:
                    i += 1
                words.append(s[start:i])
                found = False
        
    result = ' '.join(words[::-1])
    return result

            
#endregion

def test_sentenceReverse():
    stubs = [sentenceReverse0, sentenceReverse]
    for stub in stubs:    
        assert stub('This is the best') == 'best the is This'
        assert stub('Hi John,   are you ready to go?') == 'go? to ready you are John, Hi'
        assert stub('    space before') == 'before space'

sentenceReverse('abc')