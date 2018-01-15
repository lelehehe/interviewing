# http://nbviewer.jupyter.org/github/jmportilla/Python-for-Algorithms--Data-Structures--and-Interviews/blob/master/Array%20Sequences/Array%20Sequences%20Interview%20Questions/Array%20Sequence%20Interview%20Questions/Array%20Pair%20Sum%20.ipynb
def pair_sum(arr, k):
    counter = {}
    sum = 0
    for letter in arr:
        counter[letter] = 1

    for j in counter:
        l = k - j
        if counter[j] > 0 and (k - j) in counter and counter[k - j]:
            sum += 1
            counter[k - j] = 0

    return sum

# note: set() seems better instead of using dictionary {}
def pair_sum_betterVersion(arr, k):
    if len(arr) < 2:
        return 0
    seen = set()
    output = set()
    for i in arr:
        if (k - i) in seen:
            # output.add(i)
            output.add((min(i, k-i), max(i, k-i)))
        else:
            seen.add(i)
    # print('hello')
    print('\n'.join(map(str, list(output))))
    return len(output)


def test_pair_sum():
    assert pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5,
                     13, 14, 11, 13, -1], 10) == 6
    assert pair_sum([1, 2, 3, 1], 3) == 1
    assert pair_sum([1, 3, 2, 2], 4) == 2


def test_pair_sum_betterVersion():
    assert pair_sum_betterVersion(
        [1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10) == 6
    assert pair_sum_betterVersion([1, 2, 3, 1], 3) == 1
    assert pair_sum_betterVersion([1, 3, 2, 2], 4) == 2

pair_sum_betterVersion([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10)