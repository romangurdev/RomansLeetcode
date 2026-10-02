class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}                        # number → its position
        for i, n in enumerate(nums):
            need = target - n            # the number that would complete the pair
            if need in seen:             # have we seen it before?
                return [seen[need], i]
            seen[n] = i                  # remember this number and its position
