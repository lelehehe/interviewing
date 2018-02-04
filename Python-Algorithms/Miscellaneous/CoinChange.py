# Problem Statement
# .....

#region my implementation
# ============= Note ========
# use set to setup the matches pair
# use list [] as a stack
def coinChange(n, coins):
        
    # Set up our array for trakcing results
    arr = [1] + [0] * n
    
    for coin in coins:
        for i in range(coin, n + 1):
            arr[i] += arr[i - coin]
            
    if n == 0:
        return 0
    else:
        return arr[n]
#endregion

def test_coinChange():
    assert coinChange(100, [1, 2, 3]) == 884

coinChange(100, [1, 2, 3])