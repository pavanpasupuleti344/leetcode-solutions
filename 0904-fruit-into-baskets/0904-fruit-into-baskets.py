class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        i=j=0
        d={}
        maxi=0
        while(j<len(fruits)):
            d[fruits[j]]=d.get(fruits[j],0)+1
            while(len(d)>2):
                d[fruits[i]]-=1
                if d[fruits[i]]==0:
                    d.pop(fruits[i])
                i+=1
            maxi=max(maxi,j-i+1)
            j+=1
        return maxi