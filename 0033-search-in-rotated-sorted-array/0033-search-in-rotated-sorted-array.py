class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while(i<=j):
            mid=i+(j-i)//2
            if nums[mid]==target:
                return mid
            elif nums[i]<=nums[mid]:
                if nums[i]<=target<=nums[mid]:
                    j=mid-1
                    continue
                else:
                    i=mid+1
                    continue
            elif nums[j]>=nums[mid]:
                if nums[mid]<=target<=nums[j]:
                    i=mid+1
                    continue
                else:
                    j=mid-1
                    continue
        return -1