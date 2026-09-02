class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if len(nums)<(2*k)+1:return [-1]*len(nums)
        l=(2*k)+1
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        ans=[-1]*len(nums)
        # print(nums)
        ans[k]=nums[k+k]//l
        # print(ans)
        i=1
        for j in range(k+1,len(nums)-k):
            ans[j]=(nums[j+k]-nums[i-1])//l
            i+=1
        return ans