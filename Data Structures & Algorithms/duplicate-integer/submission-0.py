class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seens = set()
        for num in nums:
            if num in seens:
                return True
            seens.add(num)
        return False

    
            
        