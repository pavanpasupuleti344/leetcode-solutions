class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        while(i<j):
            mid=i+(j-i)//2
            if nums[mid]>nums[mid+1]:
                j=mid
            else:
                i=mid+1
        return i
