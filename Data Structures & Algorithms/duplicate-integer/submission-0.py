class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = {}

        for i in nums:
            if i not in mp:
                mp[i] = 1
            else:
                return True
            
        return False