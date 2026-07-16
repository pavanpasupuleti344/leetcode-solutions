class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if 0 not in nums:
            return nums
        i=nums.index(0)
        for j in range(i+1,len(nums)):
            if(nums[j]!=0):
                nums[i],nums[j]=nums[j],nums[i]
                i=nums.index(0)
        return nums