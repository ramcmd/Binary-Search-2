# TC: O(log n)
# SC: O(1)

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        
        while l < h:
            m = l + (h-l)//2
            
            if nums[m] > nums[m+1]:
                h = m
            else:
                l = m + 1
                
        return l
        