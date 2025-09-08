class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        viewed = set()
        for i in nums:
            if i in viewed:
                return True
            
            viewed.add(i)
        
        return False