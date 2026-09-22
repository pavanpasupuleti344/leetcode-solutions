class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r=[i for i in range(len(senate)) if senate[i]=='R']
        d=[i for i in range(len(senate)) if senate[i]=='D']
        # print(r,d)
        
        while len(r)!=0 and len(d)!=0:
            # print(r)
            # print(d)
            # print('------------')
            if r[0]<d[0]:
                d.pop(0)
                r.append(r[0]+len(senate))
                r.pop(0)
            else:
                r.pop(0)
                d.append(d[0]+len(senate))
                d.pop(0)
        return "Radiant" if len(d)==0 else "Dire"