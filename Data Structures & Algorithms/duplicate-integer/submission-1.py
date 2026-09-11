class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        ls = []
        for num in nums:
            if num in ls:
                return True
            else:
                ls.append(num)
        
        return False
        