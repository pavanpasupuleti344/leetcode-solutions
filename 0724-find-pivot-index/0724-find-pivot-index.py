class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # ans=-1
        left=right=0
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        for i in range(len(nums)):
            if i!=0:
                left=nums[i-1]
            if i!=len(nums)-1:
                right=nums[len(nums)-1]-nums[i]
            else:right=0
            if left==right:
                return i
        return -1