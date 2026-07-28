class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        for i in strs:
            a=list(i)
            a.sort()
            l.append("".join(a))
        print(l)
        d={}
        for i in l:
            idx=l.index(i)
            l[idx]=-1
            if i in d:
                a=d.get(i)
                a.append(strs[idx])
                d[i]=a
            else:
                d[i]=[strs[idx]]
        print(d)
        ans=[]
        for i in d.values():
            ans.append(i)
        return ans
        # j=0
        # for i in l:
        #     d[i]=d.get(i,"")+str(j)
        #     j+=1
        # print(d)
        # a=[]
        # for i in d.values():
        #     print(i)
        #     ll=[]
        #     for j in i:
        #         ll.append(strs[int(j)])
        #     a.append(ll)
        # return a