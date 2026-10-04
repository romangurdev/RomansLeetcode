#Solution 1: if statement
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0                          # best so far (safe: values are >= 1)
        for i in range(len(accounts)):      # i = each row's position
            if sum(accounts[i]) > wealth:   # is this row richer than the best?
                wealth = sum(accounts[i])   # yes → it's the new best
        return wealth                       # after the loop: the richest
        # Time: O(m × n), every number visited


#Solution 2: max()
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0                                    # best so far
        for i in range(len(accounts)):                # go through each row
            wealth = max(wealth, sum(accounts[i]))    # keep the bigger one: best vs this row
        return wealth
        # Time: O(m × n)
        # Same logic as Solution 1, written in one line


#Solution 3: fully manual (no sum, no max)
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0                    # best so far
        for row in accounts:          # row = one customer's list of money
            total = 0                 # reset for each new customer
            for money in row:         # go through each bank account
                total += money        # add it to this customer's total
            if total > wealth:        # richer than the best?
                wealth = total        # new best
        return wealth
        # Time: O(m × n)
