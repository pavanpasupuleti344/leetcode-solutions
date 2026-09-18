class Solution:
    def canJump(self, nums: list[int]) -> bool:
        if len(nums)==1:return True
        chances=nums[0]
        i=1
        while(chances>0):
            if i==(len(nums)-1):return True
            chances=max(chances-1,nums[i])
            i+=1
        return False
