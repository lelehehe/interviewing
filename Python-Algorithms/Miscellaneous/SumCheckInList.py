# Problem Statement
# Given a list of integers and a target number, write a function that returns a boolean indicating if its possible 
# to sum two intergers from th elist to reach the target number

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
def sum_check_in_list(lst, target):
    listSet = set(lst)
    for i in lst:
        if (target - i) in listSet: 
            return True
    return False

def best_solution(lst, target):
    seen = set()
    for i in lst:
        if (target - i) in seen: 
            return True
        seen.add(i)
    return False

#endregion

def test_sum_check_in_list():
    stubs = [best_solution, sum_check_in_list]
    for stub in stubs:
        assert stub([1, 3, 5, 7], 12) == True
        assert stub([1, 3, 5, 7], 5) == False
