# find squareroot of a given number rounded down to the nearest integer without using the sqrt function
# number between [9, 15] return 3
#[16, 24] returns 4

# Problem Statement
# .....

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
def fast_square_root(i):
    pass
#endregion

def test_foo():
    stubs = [fast_square_root]
    for stub in stubs:    
        assert stub(16) == 4
        assert stub(24) == 4
        assert stub(9) == 3
        assert stub(15) == 3
