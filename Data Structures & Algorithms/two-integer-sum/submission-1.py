class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i, num in enumerate(nums):
            differ = target - num
            if differ in res:
                return [res[differ], i]
            else:
                res[num] = i
