class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        i,j,maxi=0,0,0
        totsum=0
        # maxchar=''
        maxfreq=0
        while j<len(s):
            d[s[j]]=d.get(s[j],0)+1
            totsum+=1
            maxfreq=max(maxfreq,d[s[j]])
            if totsum-maxfreq > k and i <= j:
                # if d[s[i]]==maxfreq:
                #     maxfreq-=1
                d[s[i]]=d.get(s[i],0)-1
                i+=1
                totsum-=1
            maxi=max(maxi,j-i+1)
            j+=1

        return maxi




