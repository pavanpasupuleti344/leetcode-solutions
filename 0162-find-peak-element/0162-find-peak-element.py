class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        while(i<j):
            mid=i+(j-i)//2
            if i==j==mid:return i
            if nums[mid]>nums[mid+1]:
                j=mid
            else:
                i=mid+1
            # elif nums[i]>nums[mid]:
            #     if i==mid:return i
            #     else:j=mid
        return i
            # if nums[mid-1]<nums[mid]>nums[mid+1]:return mid
            # elif nums[mid-1]<nums[mid]<nums[mid+1]: i=mid+1
            # elif nums[mid-1]>nums[mid]:j=mid
