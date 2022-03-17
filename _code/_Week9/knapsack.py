def knapsack_recur(weights, values, w):
    if w == 0:
        return 0, []
    
    if len(values) == 0:
        return 0, []

    included = float("-inf")
    incl_set = []
    curr = len(values) - 1
    if weights[curr] <= w:
        included, incl_set = knapsack_recur(weights[:curr], values[:curr], w - weights[curr])
        included += values[curr]
        incl_set += [curr]

    excluded, excl_set = knapsack_recur(weights[:curr], values[:curr], w)

    if included > excluded:
        return included, incl_set 
    else:
        return excluded, excl_set

    #return max(included, excluded)

def knapsack_dp(weights, values, w):
    table = [[0 for i in range(len(values))] for i in range(w+1)]

    for i in range(w+1):
        included = float("-inf")
        incl_set = []
        curr = len(values) - 1
        if weights[curr] <= w:
            included, incl_set = table[weights[:curr], values[:curr]][ w - weights[curr]]
            included += values[curr]
            incl_set += [curr]

        excluded, excl_set = knapsack_recur(weights[:curr], values[:curr], w)

        if included > excluded:
            return included, incl_set 
        else:
            return excluded, excl_set

    #return max(included, excluded)

weights = [2, 3, 1, 5, 3]
values = [40, 50, 100, 95, 30]
print(knapsack_recur(weights, values, 10))