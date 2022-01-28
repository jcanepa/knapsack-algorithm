def knapsack_brute_force(W, weights, values, n) -> int:
    optimal_solution = None

    for i in range(n):
        pass

def knapsack_dynamic_programming(W, weights, values, n) -> int:
    '''
    Create a a two-dementional array to represent a
    memoization matrix/table: array m[0..n][0..W]
    '''
    m = [[-1 for x in range(n)] \
        for y in range(W)]

    '''
    Initialize all cells of first column and first row to -1
    '''
    # if there's no capacity then no items can be added:
    for _ in range(W): m[_][0] = 0
    # similarly, if there's no items then none can be added:
    for _ in range(n): m[0][_] = 0

    # for i from 1 to n do:
    #     for j from 0 to W do:
    #         if w[i] > j then:
    #             m[i, j] := m[i-1, j]
    #         else:
    #             m[i, j] := max(m[i-1, j], m[i-1, j-w[i]] + v[i])
    for _ in m:
        print(_)


if __name__ == '__main__':

    # knapsack weight capacity
    capacity = 50
    weights = [10, 20, 30]
    values  = [50, 100, 150]
    # n is the number of distinct items
    n = len(values)

    # print(knapsack_brute_force(capacity, weights, values, n))
    print(knapsack_dynamic_programming(capacity, weights, values, n))