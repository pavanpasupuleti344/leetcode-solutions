class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # win={}
        # lost={}
        d={}
        for i in matches:
            d[i[1]]=d.get(i[1],0)+1
        # print(d)
        s=[x for x in d.keys() if d[x]==1]
        # print(s)
        f=[x[0] for x in matches if x[0] not in d]
        # print(f)
        # f=list(map(lambda x:x[0] if x not in d))
        ans=[sorted(set(f)),sorted(set(s))]
        return ans