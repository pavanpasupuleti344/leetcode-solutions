class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        for i in range(len(nums)):
            if i==0:
                prefix[i]=nums[i]
                continue
            prefix[i]=prefix[i-1]*nums[i]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                suffix[i]=nums[i]
                continue
            suffix[i]=suffix[i+1]*nums[i]
        nums[0]=suffix[1]
        nums[-1]=prefix[-2]
        for i in range(1,len(nums)-1):
            nums[i]=prefix[i-1]*suffix[i+1]
        return nums