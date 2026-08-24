class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        while i<j:
            mid=i+(j-i)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                j=mid
            else:
                i=mid+1
        return i+(j-i)//2 if nums[i+(j-i)//2]==target else -1
