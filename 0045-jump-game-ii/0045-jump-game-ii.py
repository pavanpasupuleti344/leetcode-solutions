class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums)==1:return 0
        jumps=1
        chances=nums[0]
        i=1
        max_shift=pos=-1
        while(chances > 0):
            # if (chances+i)>=(len(nums)-1):return jumps
            chances-=1
            if (chances+i)>=(len(nums)-1):return jumps
            if nums[i]>chances:
                if (nums[i]+i)>max_shift:
                    max_shift=i+nums[i]
                    pos=i
            i+=1
            if chances==0:
                jumps+=1
                chances=nums[pos]
                i=pos+1
            

