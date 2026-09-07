class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l=max(i[2] for i in trips)
        ans=[0]*(l+1)
        for i in trips:
            ans[i[1]]+=i[0]
            ans[i[2]]+=i[0]*-1
        print(ans)
        if ans[0]>capacity:return False
        for i in range(1,len(ans)):
            ans[i]+=ans[i-1]
            if ans[i]>capacity:return False
        return True

