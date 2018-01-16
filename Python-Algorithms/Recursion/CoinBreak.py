# Problem Statement
# .....

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack

def findOneCoin(n, coins):
    for coin in coins:
        if n > coin:
            return coin
    return 0

def coin_break(n, coins):
    if n in coins: 
        return 1

    m = findOneCoin(n, coins)
    return 1 + coin_break(n - m, coins)
#endregion

def test_coin_break():
    stubs = [coin_break]
    for stub in stubs:    
        assert stub(10, [5,2,1]) == 2
        assert stub(12, [5,2,1]) == 3
        assert stub(74, [25,10,5,1]) == 8
