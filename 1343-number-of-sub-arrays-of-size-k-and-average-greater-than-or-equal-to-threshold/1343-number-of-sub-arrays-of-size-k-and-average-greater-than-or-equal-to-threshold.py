class Solution:
    def numOfSubarrays(self, nums: List[int], k: int, threshold: int) -> int:
        c=0
        sum=0
        for i in range(k):
            sum+=nums[i]    
        i,j=1,k
        maxi=(sum/k)
        if maxi>=threshold:
            c+=1
        while(j<len(nums)):
            sum=sum-nums[i-1]+nums[j]
            i+=1
            j+=1
            avg=sum/k
            if avg>=threshold:
                maxi=max(maxi,avg)
                c+=1
        return c