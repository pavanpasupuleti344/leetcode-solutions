class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i,j=0,0
        zero=0
        maxi=0
        while j<len(nums):
            if nums[j]==0:
                zero+=1
            while zero>k :
                if nums[i]==0:
                    zero-=1
                    i+=1
                else:
                    i+=1
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi