class Solution:
    def shipWithinDays(self, nums: List[int], days: int) -> int:
        i=max(nums)
        j=sum(nums)
        while(i<j):
            mid=i+(j-i)//2
            count=0
            sumi=0
            for k in nums:
                sumi+=k
                if sumi<mid:continue
                if sumi==mid:
                    count+=1
                    sumi=0
                elif sumi>mid:
                    count+=1
                    sumi=k
            if sumi!=0:count+=1
            if count>days:
                i=mid+1
            else:
                j=mid
        return i