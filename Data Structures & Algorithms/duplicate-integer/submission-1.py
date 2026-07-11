class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        Map = {} #value: index

        for i, num in enumerate(nums):
            if nums[i] in Map:
                return True
            else:
                 Map[num] = i

        return False
            
