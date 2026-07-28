class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum=0
        for i in range(k):
            sum+=nums[i]
        maxi,i,j=sum,1,k
        while(i<(len(nums)-k+1)):
            sum=sum-nums[i-1]+nums[j]
            i+=1
            j+=1
            maxi=max(maxi,sum)
        return maxi/k