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
    Create a a two-dementional array to represent a
    memoization matrix/table: array m[0..W][0..n] is accessed as: m[column][row]
    '''
    m = [[-1 for x in range(n)] \
        for y in range(W)]

    '''
    Initialize all cells of first column and first row to 0:
    first, if there's no capacity then no items can be added
    similarly, if there's no items then none can be added
    '''
    for _ in range(W): m[_][0] = 0
    for _ in range(n): m[0][_] = 0

    for i in range(1, n):
        for j in range(1, W):
            if weights[i] > j:
                # m[i, j] := m[i-1, j]
                m[j][i] = m[j-1][i]
            else:
                # m[i, j] := max(m[i-1, j], m[i-1, j-w[i]] + v[i])
                m[j][i] = max(
                            m[j-1][i],
                            m[j-1][i-weights[j]] + values[i])

    for _ in m:
        print(_)


if __name__ == '__main__':

    # knapsack weight capacity
    capacity = 50
    weights = [10, 20, 30]
    values  = [50, 100, 150]
    # n is the number of distinct items
    n = len(values)

    print(knapsack_brute_force(capacity, weights, values, n))
    # print(knapsack_dynamic_programming(capacity, weights, values, n))