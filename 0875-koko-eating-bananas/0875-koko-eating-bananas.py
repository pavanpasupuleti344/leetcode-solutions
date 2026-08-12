class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        ans=0
        # l=[i for i in range(1,max(piles)+1)]
        i=1
        j=max(piles)
        while i<j:
            mid=i+(j-i)//2
            ans=0
            for k in piles:
                ans+=(k+mid-1)//mid
            # if ans==h:
            #     mini=min(mini,l[mid])
            #     j=mid
            if ans>h:
                i=mid+1
            else:
                j=mid
        return i