class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # s=set(sorted(nums))
        i=j=-1
        for k in range(len(nums)-1):
            # if any(x<nums[k] in s):
            if nums[k]>min(nums[k+1:]):
                i=k
                break
        for k in range(len(nums)-1,0,-1):
            if nums[k]<max(nums[:k]):
                j=k
                break
        if i==j==-1:return 0
        if i==j:return len(nums)-j
        return j-i+1