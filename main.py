def knapsack_brute_force(W, weights, values, n) -> int:
    # base cases: no items or no capacity
    if (n < 1): return 0
    if (W < 1): return 0

    # if the item at the last index cannot be included,
    # recurse on a subset of the collection
    if weights[n-1] > W:
        return knapsack_brute_force(
            W, weights, values, n-1)

    # should the last item in the set be added?
    # if yes, add it and subtract its weight from the capacity
    # otherwise skip it and continue considering the subset of smaller indices
    added   = knapsack_brute_force(W-weights[n-1], weights, values, n-1) + values[n-1]
    skipped = knapsack_brute_force(W, weights, values, n-1)

    # return the optimal solution
    return max(
        added, skipped)

def knapsack_dynamic_programming(W, weights, values, n) -> int:
    '''
    Create a a two-dementional array to represent a table:
    array m[0..W][0..n] is accessed as: m[row][column]
    '''
    m = [[-1 for x in range(W+1)] \
        for y in range(n+1)]

    '''
    Initialize all cells of first column and first row to 0:
    because if there's no capacity then no items can be added
    similarly, if there's no items then none can be added
    '''
    for _ in range(n+1): m[_][0] = 0
    for _ in range(W+1): m[0][_] = 0

    for i in range(1, n+1):
        for j in range(1, W+1):
            if weights[i-1] <= j:
                m[i][j] = max(
                            m[i-1][j],
                            m[i-1][j-weights[i-1]] + values[i-1])
            else:
                m[i][j] = m[i-1][j]
    return m[-1][-1]

'''
Abdul Bari method: https://www.youtube.com/watch?v=zRza99HPvkQ
'''
def knapsack_dp_tabulation(m, w, p, n):
    pass


if __name__ == '__main__':

    # knapsack weight capacity
    capacity = 50
    weights = [10, 20, 30]
    values  = [50, 100, 150]
    # n is the number of distinct items
    n = len(values)
    print(knapsack_brute_force(capacity, weights, values, n))

    print(knapsack_dynamic_programming(capacity, weights, values, n))
    # print(knapsack_dp_tabulation())