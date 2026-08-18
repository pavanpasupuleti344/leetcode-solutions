class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=len(nums)+2
        csum=0
        i,j=0,0
        while j<len(nums):
            csum+=nums[j]
            while i<=j and csum>=target:
                mini=min(mini,j-i+1)
                csum-=nums[i]
                i+=1
            j+=1
            
        if mini==len(nums)+2:
            return 0
        else:
            return mini