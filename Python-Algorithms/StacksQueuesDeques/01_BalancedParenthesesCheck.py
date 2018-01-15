# Problem Statement
# Given a string of opening and closing parentheses, check whether it’s balanced. 
# We have 3 types of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. 
# Assume that the string doesn’t contain any other character than these, no spaces words or numbers. 
# As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse 
# order opened. For example ‘([])’ is balanced but ‘([)]’ is not.
# You can assume the input string has no spaces.

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
def balance_check(s):
    def isMatch(c1, c2):
        matches = set([('(',')'),('{','}'),('[',']')])
        if (c1, c2) in matches:
            return True
        return False 
            
    if len(s) % 2 != 0: 
        return False
    
    stack = []
    # opens = set('{[(')
    for c in s:
        if len(stack) != 0 and isMatch(stack[-1], c):
            stack.pop()
        else: 
            stack.append(c)
    return len(stack) == 0
#endregion

def test_balance_check():
    stubs = [balance_check]
    for stub in stubs:    
        assert stub('[](){([[[]]])}(') == False
        assert stub('[{{{(())}}}]((()))') == True
        assert stub('[[[]])]') == False
        assert stub('][()') == False
        assert stub('[][()]') == True