# Problem Statement
# .....

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
def foo(s):
    pass
#endregion

def test_foo():
    stubs = [foo]
    for stub in stubs:    
        assert stub('[](){([[[]]])}(') == False
