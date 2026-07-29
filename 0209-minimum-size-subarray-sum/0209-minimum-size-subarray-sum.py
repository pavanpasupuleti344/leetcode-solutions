class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mini=len(nums)+2
        sum=0
        i,j=0,0
        while j<len(nums):
            if i==j:
                sum=nums[i]
            else:
                sum+=nums[j]
            while i<=j and sum>=target:
                mini=min(mini,j-i+1)
                sum-=nums[i]
                i+=1
            j+=1
            
        if mini==len(nums)+2:
            return 0
        else:
            return mini