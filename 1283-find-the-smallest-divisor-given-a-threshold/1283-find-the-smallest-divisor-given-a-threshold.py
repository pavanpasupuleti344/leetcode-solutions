class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        i=1
        j=sum(nums)
        mini=j
        while i<j:
            mid=i+(j-i)//2
            ans=0
            for k in nums:
                ans+=math.ceil(k/mid)
                if ans>threshold:
                    break
            if ans<=threshold:
                mini=min(mini,mid)
                j=mid
            else:
                i=mid+1
        ans=0
        for k in nums:
            ans+=round(k/i)
        if ans<=threshold:
            mini=min(mini,i)
        return mini
