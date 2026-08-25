class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        ans=[0]*(n+1)
        for a,b,c in bookings:
            ans[a-1]+=c
            ans[b]-=c
        for i in range(len(ans)):
            if i!=0:
                ans[i]+=ans[i-1]
        return ans[:-1]
    
