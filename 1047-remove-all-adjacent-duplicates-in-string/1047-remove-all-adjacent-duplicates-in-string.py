class Solution:
    def removeDuplicates(self, s: str) -> str:
        ans=[]
        for i in s:
            if len(ans)==0:
                ans.append(i)
                # print(ans,'New element')
                continue
            if ans[-1]==i:
                # print(ans,i,'befor pop')
                ans.pop()
                # print(ans,'after pop')
            else:
                ans.append(i)
                # print(ans)
        return ''.join(ans)
            