# Problem Statement
# Given a list of account ID numbers (int) which contains all duplicates except one unique, find the one 
# unique integer. The list is guaranteed to only have one unique no -duplicated int.
# Reference for dictionary: 
# https://www.programiz.com/python-programming/dictionary#change

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
def unique_id(lst):
    dct = {}
    for i in lst:
        if i in dct:
            dct[i] = True
        else:
            dct[i] = False
    for key in dct:
        if dct[key] == False:
            return key

    return 1

def unique_id_XOR(lst):
    seed = 0
    for i in lst:
        seed ^= i
    return seed
#endregion

def test_unique_id():
    stubs = [unique_id]
    for stub in stubs:    
        assert stub([1, 2, 3, 4, 6, 1, 2, 3, 4, 5, 6]) == 5
        assert stub([1, 2, 3, 2, 1]) == 3

result = unique_id([1, 2, 3, 4, 6, 1, 2, 3, 4, 5, 6])
