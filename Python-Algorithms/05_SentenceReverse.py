# reverse all the words in sentence.
# Given:
#   'This is the best'
# Return:
#   'best the is This'

#region my implementation
def sentenceReverse(s):
    #1 get words from sentence
    return " ".join(reversed(s.split()))

#endregion

def test_sentenceReverse():
    assert sentenceReverse('This is the best') == 'best the is This'
    assert sentenceReverse('Hi John,   are you ready to go?') == 'go? to ready you are John, Hi'
    assert sentenceReverse('    space before') == 'before space'
