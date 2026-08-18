class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0
        j=len(nums)-1
        mini=sys.maxsize
        while(i<=j):
            mid=i+(j-i)//2
            mini=min(mini,nums[mid])
            if nums[mid]<=nums[j]:
                mini=min(mini,nums[mid])
                j=mid-1
            elif nums[i]<=nums[mid]:
                mini=min(mini,nums[i])
                i=mid+1
        return mini
