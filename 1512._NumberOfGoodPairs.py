# 1512. Number of Good Pairs (Easy)
# Count pairs (i, j) where nums[i] == nums[j] and i < j.

from typing import List


# Solution 1: Brute force, two loops
# Time: O(n^2)  Space: O(1)
class Solution1:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c = 0
        for i in range(len(nums)):              # pick each item
            for j in range(i + 1, len(nums)):   # compare with every item after it
                if nums[i] == nums[j]:          # same value = good pair
                    c += 1
        return c


# Solution 2: Sort first, so equal numbers sit next to each other
# Time: O(n log n)  Space: O(n)
class Solution2:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        nums = sorted(nums)     # [1,2,3,1,1,3] -> [1,1,1,2,3,3]
        c = 0
        run = 1                 # how many equal numbers we've seen in a row
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:  # same as the one before?
                c += run                # it pairs with every equal one before it
                run += 1
            else:
                run = 1                 # new number, restart the count
        return c


# Solution 3: Dictionary, count as we go
# Time: O(n)  Space: O(n)
class Solution3:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}               # number -> how many times we've seen it so far
        c = 0
        for n in nums:
            c += seen.get(n, 0)             # n pairs with every earlier copy of itself
            seen[n] = seen.get(n, 0) + 1    # now count this one too
        return c


# Tests (all three should print 4)
nums = [1, 2, 3, 1, 1, 3]
print(Solution1().numIdenticalPairs(nums))
print(Solution2().numIdenticalPairs(nums))
print(Solution3().numIdenticalPairs(nums))